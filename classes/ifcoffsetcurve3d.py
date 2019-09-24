class IFCOFFSETCURVE3D(IFCCURVE):
	def __init__(self, BasisCurve, Distance, SelfIntersect, RefDirection):
		 self.BasisCurve = BasisCurve
		 self.Distance = Distance
		 self.SelfIntersect = SelfIntersect
		 self.RefDirection = RefDirection