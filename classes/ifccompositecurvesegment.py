class IFCCOMPOSITECURVESEGMENT(IFCGEOMETRICREPRESENTATIONITEM):
	def __init__(self, Transition, SameSense, ParentCurve):
		 self.Transition = Transition
		 self.SameSense = SameSense
		 self.ParentCurve = ParentCurve