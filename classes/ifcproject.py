class IFCPROJECT(IFCOBJECT):
	def __init__(self, LongName, Phase, RepresentationContexts, UnitsInContext):
		 self.LongName = LongName
		 self.Phase = Phase
		 self.RepresentationContexts = RepresentationContexts
		 self.UnitsInContext = UnitsInContext