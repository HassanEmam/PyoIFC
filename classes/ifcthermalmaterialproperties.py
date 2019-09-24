class IFCTHERMALMATERIALPROPERTIES(IFCMATERIALPROPERTIES):
	def __init__(self, SpecificHeatCapacity, BoilingPoint, FreezingPoint, ThermalConductivity):
		 self.SpecificHeatCapacity = SpecificHeatCapacity
		 self.BoilingPoint = BoilingPoint
		 self.FreezingPoint = FreezingPoint
		 self.ThermalConductivity = ThermalConductivity