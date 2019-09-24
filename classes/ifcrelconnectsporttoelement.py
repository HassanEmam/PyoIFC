class IFCRELCONNECTSPORTTOELEMENT(IFCRELCONNECTS):
	def __init__(self, RelatingPort, RelatedElement):
		 self.RelatingPort = RelatingPort
		 self.RelatedElement = RelatedElement