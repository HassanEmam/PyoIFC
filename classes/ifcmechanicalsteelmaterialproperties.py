class IFCMECHANICALSTEELMATERIALPROPERTIES(IFCMECHANICALMATERIALPROPERTIES):
	def __init__(self, YieldStress, UltimateStress, UltimateStrain, HardeningModule, ProportionalStress, PlasticStrain, Relaxations):
		 self.YieldStress = YieldStress
		 self.UltimateStress = UltimateStress
		 self.UltimateStrain = UltimateStrain
		 self.HardeningModule = HardeningModule
		 self.ProportionalStress = ProportionalStress
		 self.PlasticStrain = PlasticStrain
		 self.Relaxations = Relaxations