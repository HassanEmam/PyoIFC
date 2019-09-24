class IFCRELSPACEBOUNDARY(IFCRELCONNECTS):
	def __init__(self, RelatingSpace, RelatedBuildingElement, ConnectionGeometry, PhysicalOrVirtualBoundary, InternalOrExternalBoundary):
		 self.RelatingSpace = RelatingSpace
		 self.RelatedBuildingElement = RelatedBuildingElement
		 self.ConnectionGeometry = ConnectionGeometry
		 self.PhysicalOrVirtualBoundary = PhysicalOrVirtualBoundary
		 self.InternalOrExternalBoundary = InternalOrExternalBoundary