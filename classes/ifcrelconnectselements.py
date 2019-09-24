class IFCRELCONNECTSELEMENTS(IFCRELCONNECTS):
	def __init__(self, ConnectionGeometry, RelatingElement, RelatedElement):
		 self.ConnectionGeometry = ConnectionGeometry
		 self.RelatingElement = RelatingElement
		 self.RelatedElement = RelatedElement