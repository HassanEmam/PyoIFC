class IFCCONSTRUCTIONRESOURCE(IFCRESOURCE):
	def __init__(self, ResourceIdentifier, ResourceGroup, ResourceConsumption, BaseQuantity):
		 self.ResourceIdentifier = ResourceIdentifier
		 self.ResourceGroup = ResourceGroup
		 self.ResourceConsumption = ResourceConsumption
		 self.BaseQuantity = BaseQuantity