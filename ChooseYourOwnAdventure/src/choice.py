from pyio import *

class choice:

	def __init__(self):
		self.title = None
		self.text = None
		self.id = 0
		# Add self.choices vector

	def setId(self, newval):
		self.id = newval

	def setTitle(self, newval):
		self.title = newval

	def getTitle(self):
		return self.title
	
	def setText(self, newval):
		self.text = newval

	#def __init__(self):

	def addChoice(self, the_choice):
		self.choices.append(the_choice)

	def prompt(self):
                self.choices = []

		for choiceX in self.choices:
			pyout(self.id)
			pyout(") ")
			pyout(choiceX.title)
			pyout(endl)

		inpvar = None
		pyin(inpvar)
		for choiceY in self.choices:
			if choiceY.id == inpvar.strip()[0]:
				return choiceY
		return self
