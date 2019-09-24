class IFCLIGHTSOURCEPOSITIONAL(IFCLIGHTSOURCE):
	def __init__(self, Position, Radius, ConstantAttenuation, DistanceAttenuation, QuadricAttenuation):
		 self.Position = Position
		 self.Radius = Radius
		 self.ConstantAttenuation = ConstantAttenuation
		 self.DistanceAttenuation = DistanceAttenuation
		 self.QuadricAttenuation = QuadricAttenuation