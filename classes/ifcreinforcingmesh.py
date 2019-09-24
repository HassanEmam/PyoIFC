class IFCREINFORCINGMESH(IFCREINFORCINGELEMENT):
	def __init__(self, MeshLength, MeshWidth, LongitudinalBarNominalDiameter, TransverseBarNominalDiameter, LongitudinalBarCrossSectionArea, TransverseBarCrossSectionArea, LongitudinalBarSpacing, TransverseBarSpacing):
		 self.MeshLength = MeshLength
		 self.MeshWidth = MeshWidth
		 self.LongitudinalBarNominalDiameter = LongitudinalBarNominalDiameter
		 self.TransverseBarNominalDiameter = TransverseBarNominalDiameter
		 self.LongitudinalBarCrossSectionArea = LongitudinalBarCrossSectionArea
		 self.TransverseBarCrossSectionArea = TransverseBarCrossSectionArea
		 self.LongitudinalBarSpacing = LongitudinalBarSpacing
		 self.TransverseBarSpacing = TransverseBarSpacing