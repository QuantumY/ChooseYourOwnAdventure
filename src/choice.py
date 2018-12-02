from pyio import *

class choice:

	def __init__(self):
		self.title = None
		self.text = None
		self.userSelectText = None
		self.choices = []
		# Add self.choices vector

	def setTitle(self, newval):
		self.title = newval

	def getTitle(self):
		return self.title

	def setText(self, newval):
		self.text = newval

	def setUserSelectText(self, newval):
		self.userSelectText = newval

	def getText(self):
		return self.text

	def addChoice(self, the_choice):
		self.choices.append(the_choice)

	def echo(self, n = 0):
		print n
		print "-------------------"
		print "Title: " + self.title
		print "Description: " + self.text
		print "-------------------"

		n = n + 1

		print "Children ---------->>>>>>>>>>>>>>"
		for choice in self.choices:
			choice.echo(n)

	def collectUserInput(self):
		usersChoice = input("Please Choose: ")

		return int(usersChoice)


	def prompt(self):
		pyout(self.getTitle())
		pyout("\n")
		pyout(self.getText())
		pyout("\n")
		pyout("\n")

		cc = 1
		for choice in self.choices:
			pyout(str(cc)+" : "+choice.getTitle()+"\n")
			cc = cc + 1

		pyout(str(cc)+" : Quit\n")

		usersChoice = 0

		while usersChoice <= 0 or usersChoice > cc:
			usersChoice = self.collectUserInput()

		if usersChoice == cc:
			pyout("\nBye!\n")
		else:
			self.choices[usersChoice].prompt()
		

