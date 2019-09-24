class IFCCURVEBOUNDEDPLANE(IFCBOUNDEDSURFACE):
	def __init__(self, BasisSurface, OuterBoundary, InnerBoundaries):
		 self.BasisSurface = BasisSurface
		 self.OuterBoundary = OuterBoundary
		 self.InnerBoundaries = InnerBoundaries