class IFCSWEPTDISKSOLID(IFCSOLIDMODEL):
	def __init__(self, Directrix, Radius, InnerRadius, StartParam, EndParam):
		 self.Directrix = Directrix
		 self.Radius = Radius
		 self.InnerRadius = InnerRadius
		 self.StartParam = StartParam
		 self.EndParam = EndParam