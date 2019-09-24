class IFCRECTANGULARTRIMMEDSURFACE(IFCBOUNDEDSURFACE):
	def __init__(self, BasisSurface, U1, V1, U2, V2, Usense, Vsense):
		 self.BasisSurface = BasisSurface
		 self.U1 = U1
		 self.V1 = V1
		 self.U2 = U2
		 self.V2 = V2
		 self.Usense = Usense
		 self.Vsense = Vsense