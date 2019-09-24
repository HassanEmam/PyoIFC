class IFCELECTRICALBASEPROPERTIES(IFCENERGYPROPERTIES):
	def __init__(self, ElectricCurrentType, InputVoltage, InputFrequency, FullLoadCurrent, MinimumCircuitCurrent, MaximumPowerInput, RatedPowerInput, InputPhase):
		 self.ElectricCurrentType = ElectricCurrentType
		 self.InputVoltage = InputVoltage
		 self.InputFrequency = InputFrequency
		 self.FullLoadCurrent = FullLoadCurrent
		 self.MinimumCircuitCurrent = MinimumCircuitCurrent
		 self.MaximumPowerInput = MaximumPowerInput
		 self.RatedPowerInput = RatedPowerInput
		 self.InputPhase = InputPhase