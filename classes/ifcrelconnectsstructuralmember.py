class IFCRELCONNECTSSTRUCTURALMEMBER(IFCRELCONNECTS):
	def __init__(self, RelatingStructuralMember, RelatedStructuralConnection, AppliedCondition, AdditionalConditions, SupportedLength, ConditionCoordinateSystem):
		 self.RelatingStructuralMember = RelatingStructuralMember
		 self.RelatedStructuralConnection = RelatedStructuralConnection
		 self.AppliedCondition = AppliedCondition
		 self.AdditionalConditions = AdditionalConditions
		 self.SupportedLength = SupportedLength
		 self.ConditionCoordinateSystem = ConditionCoordinateSystem