class choice:

	def __init__(self):
		self.userSelectText = None
		self.scenario = None

	def setScenario(self, scenario):
		self.scenario = scenario

	def setUserSelectText(self, newval):
		self.userSelectText = newval

	def getUserSelectText(self):
		return self.userSelectText

	def prompt(self):
		self.scenario.prompt()

	def echo(self, n = 0):
		print n
		print "-------------------"
		print "User Select Text: " + self.userSelectText
		print "-------------------"

		n = n + 1



