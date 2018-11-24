import pyio

class choice:
	def setId(self, newval):
		self.id = newval

	def setTitle(self, newval):
		self.title = newval
	
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

		inpvar;	#input variable
		pyin(inpvar)
		for choiceY in self.choices:
			if choiceY.id == inpvar.strip()[0]:
				return choiceY
		return self
