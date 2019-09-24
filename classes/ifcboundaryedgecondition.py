class IFCBOUNDARYEDGECONDITION(IFCBOUNDARYCONDITION):
	def __init__(self, LinearStiffnessByLengthX, LinearStiffnessByLengthY, LinearStiffnessByLengthZ, RotationalStiffnessByLengthX, RotationalStiffnessByLengthY, RotationalStiffnessByLengthZ):
		 self.LinearStiffnessByLengthX = LinearStiffnessByLengthX
		 self.LinearStiffnessByLengthY = LinearStiffnessByLengthY
		 self.LinearStiffnessByLengthZ = LinearStiffnessByLengthZ
		 self.RotationalStiffnessByLengthX = RotationalStiffnessByLengthX
		 self.RotationalStiffnessByLengthY = RotationalStiffnessByLengthY
		 self.RotationalStiffnessByLengthZ = RotationalStiffnessByLengthZ