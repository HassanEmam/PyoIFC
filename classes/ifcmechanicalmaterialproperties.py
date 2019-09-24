class IFCMECHANICALMATERIALPROPERTIES(IFCMATERIALPROPERTIES):
	def __init__(self, DynamicViscosity, YoungModulus, ShearModulus, PoissonRatio, ThermalExpansionCoefficient):
		 self.DynamicViscosity = DynamicViscosity
		 self.YoungModulus = YoungModulus
		 self.ShearModulus = ShearModulus
		 self.PoissonRatio = PoissonRatio
		 self.ThermalExpansionCoefficient = ThermalExpansionCoefficient