class IFCGEOMETRICREPRESENTATIONCONTEXT(IFCREPRESENTATIONCONTEXT):
	def __init__(self, CoordinateSpaceDimension, Precision, WorldCoordinateSystem, TrueNorth):
		 self.CoordinateSpaceDimension = CoordinateSpaceDimension
		 self.Precision = Precision
		 self.WorldCoordinateSystem = WorldCoordinateSystem
		 self.TrueNorth = TrueNorth