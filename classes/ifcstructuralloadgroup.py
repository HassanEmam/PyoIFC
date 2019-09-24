class IFCSTRUCTURALLOADGROUP(IFCGROUP):
	def __init__(self, PredefinedType, ActionType, ActionSource, Coefficient, Purpose):
		 self.PredefinedType = PredefinedType
		 self.ActionType = ActionType
		 self.ActionSource = ActionSource
		 self.Coefficient = Coefficient
		 self.Purpose = Purpose