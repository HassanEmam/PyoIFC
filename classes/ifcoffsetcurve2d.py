class IFCOFFSETCURVE2D(IFCCURVE):
	def __init__(self, BasisCurve, Distance, SelfIntersect):
		 self.BasisCurve = BasisCurve
		 self.Distance = Distance
		 self.SelfIntersect = SelfIntersect