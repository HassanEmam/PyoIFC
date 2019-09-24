class IFCPOINTONSURFACE(IFCPOINT):
	def __init__(self, BasisSurface, PointParameterU, PointParameterV):
		 self.BasisSurface = BasisSurface
		 self.PointParameterU = PointParameterU
		 self.PointParameterV = PointParameterV