from pyio import *

class choice:

	def __init__(self):
		self.title = None
		self.text = None
		self.choices = []
		# Add self.choices vector

	def setTitle(self, newval):
		self.title = newval

	def getTitle(self):
		return self.title

	def setText(self, newval):
		self.text = newval

	#def __init__(self):

	def addChoice(self, the_choice):
		self.choices.append(the_choice)

	def echo(self):
		pyout("-------------------\n")
		pyout(self.title + '\n')
		pyout(self.text + '\n')
		pyout("-------------------\n")

		for choiceY in self.choices:
			choiceY.echo()

	def prompt(self):

		for choiceX in self.choices:
			pyout(") ")
			pyout(choiceX.title)
			pyout(endl)

		inpvar = pyget()
		return self.choices[inpvar.strip()[0]] #Bug
