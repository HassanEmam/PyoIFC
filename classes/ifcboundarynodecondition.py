class IFCBOUNDARYNODECONDITION(IFCBOUNDARYCONDITION):
	def __init__(self, LinearStiffnessX, LinearStiffnessY, LinearStiffnessZ, RotationalStiffnessX, RotationalStiffnessY, RotationalStiffnessZ):
		 self.LinearStiffnessX = LinearStiffnessX
		 self.LinearStiffnessY = LinearStiffnessY
		 self.LinearStiffnessZ = LinearStiffnessZ
		 self.RotationalStiffnessX = RotationalStiffnessX
		 self.RotationalStiffnessY = RotationalStiffnessY
		 self.RotationalStiffnessZ = RotationalStiffnessZ