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

	def prompt(self):

		for choiceX in self.choices:
			pyout(") ")
			pyout(choiceX.title)
			pyout(endl)

		inpvar = None
		pyin(inpvar)
		return self.choices[inpvar.strip()[0]] #Bug
