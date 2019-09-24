class IFCSTRUCTURALLOADSINGLEFORCE(IFCSTRUCTURALLOADSTATIC):
	def __init__(self, ForceX, ForceY, ForceZ, MomentX, MomentY, MomentZ):
		 self.ForceX = ForceX
		 self.ForceY = ForceY
		 self.ForceZ = ForceZ
		 self.MomentX = MomentX
		 self.MomentY = MomentY
		 self.MomentZ = MomentZ