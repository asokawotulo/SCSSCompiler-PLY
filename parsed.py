class ParsedObject():
	def __init__(self):
		self.text = ""
		self.converted = ""
		self.success = False
		self.selectors = []
		self.properties = []

	def addSelector(self, var):
		self.selectors.append(var)

	def addProperty(self, var):
		self.properties.append(var)

	def setText(self, var):
		self.text = var

	def setSuccess(self, var):
		self.success = var

	def writeConverted(self, var):
		self.converted += var