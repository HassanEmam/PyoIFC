class IFCSTRUCTURALRESULTGROUP(IFCGROUP):
	def __init__(self, TheoryType, ResultForLoadGroup, IsLinear):
		 self.TheoryType = TheoryType
		 self.ResultForLoadGroup = ResultForLoadGroup
		 self.IsLinear = IsLinear