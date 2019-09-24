class IFCWATERPROPERTIES(IFCMATERIALPROPERTIES):
	def __init__(self, IsPotable, Hardness, AlkalinityConcentration, AcidityConcentration, ImpuritiesContent, PHLevel, DissolvedSolidsContent):
		 self.IsPotable = IsPotable
		 self.Hardness = Hardness
		 self.AlkalinityConcentration = AlkalinityConcentration
		 self.AcidityConcentration = AcidityConcentration
		 self.ImpuritiesContent = ImpuritiesContent
		 self.PHLevel = PHLevel
		 self.DissolvedSolidsContent = DissolvedSolidsContent