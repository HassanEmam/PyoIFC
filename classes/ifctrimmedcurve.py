class IFCTRIMMEDCURVE(IFCBOUNDEDCURVE):
	def __init__(self, BasisCurve, Trim1, Trim2, SenseAgreement, MasterRepresentation):
		 self.BasisCurve = BasisCurve
		 self.Trim1 = Trim1
		 self.Trim2 = Trim2
		 self.SenseAgreement = SenseAgreement
		 self.MasterRepresentation = MasterRepresentation