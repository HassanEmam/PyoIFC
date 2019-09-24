class IFCTENDON(IFCREINFORCINGELEMENT):
	def __init__(self, PredefinedType, NominalDiameter, CrossSectionArea, TensionForce, PreStress, FrictionCoefficient, AnchorageSlip, MinCurvatureRadius):
		 self.PredefinedType = PredefinedType
		 self.NominalDiameter = NominalDiameter
		 self.CrossSectionArea = CrossSectionArea
		 self.TensionForce = TensionForce
		 self.PreStress = PreStress
		 self.FrictionCoefficient = FrictionCoefficient
		 self.AnchorageSlip = AnchorageSlip
		 self.MinCurvatureRadius = MinCurvatureRadius