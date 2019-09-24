class IFCCOMPOSITECURVE(IFCBOUNDEDCURVE):
	def __init__(self, Segments, SelfIntersect):
		 self.Segments = Segments
		 self.SelfIntersect = SelfIntersect