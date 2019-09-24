class IFCSURFACECURVESWEPTAREASOLID(IFCSWEPTAREASOLID):
	def __init__(self, Directrix, StartParam, EndParam, ReferenceSurface):
		 self.Directrix = Directrix
		 self.StartParam = StartParam
		 self.EndParam = EndParam
		 self.ReferenceSurface = ReferenceSurface