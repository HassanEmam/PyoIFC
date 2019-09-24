class IFCRELCONNECTSPORTS(IFCRELCONNECTS):
	def __init__(self, RelatingPort, RelatedPort, RealizingElement):
		 self.RelatingPort = RelatingPort
		 self.RelatedPort = RelatedPort
		 self.RealizingElement = RealizingElement