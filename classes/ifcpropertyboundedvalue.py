class IFCPROPERTYBOUNDEDVALUE(IFCSIMPLEPROPERTY):
	def __init__(self, UpperBoundValue, LowerBoundValue, Unit):
		 self.UpperBoundValue = UpperBoundValue
		 self.LowerBoundValue = LowerBoundValue
		 self.Unit = Unit