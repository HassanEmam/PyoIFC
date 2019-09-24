class IFCSTRUCTURALLOADTEMPERATURE(IFCSTRUCTURALLOADSTATIC):
	def __init__(self, DeltaT_Constant, DeltaT_Y, DeltaT_Z):
		 self.DeltaT_Constant = DeltaT_Constant
		 self.DeltaT_Y = DeltaT_Y
		 self.DeltaT_Z = DeltaT_Z