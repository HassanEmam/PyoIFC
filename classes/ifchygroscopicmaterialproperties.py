class IFCHYGROSCOPICMATERIALPROPERTIES(IFCMATERIALPROPERTIES):
	def __init__(self, UpperVaporResistanceFactor, LowerVaporResistanceFactor, IsothermalMoistureCapacity, VaporPermeability, MoistureDiffusivity):
		 self.UpperVaporResistanceFactor = UpperVaporResistanceFactor
		 self.LowerVaporResistanceFactor = LowerVaporResistanceFactor
		 self.IsothermalMoistureCapacity = IsothermalMoistureCapacity
		 self.VaporPermeability = VaporPermeability
		 self.MoistureDiffusivity = MoistureDiffusivity