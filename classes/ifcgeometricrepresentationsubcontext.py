class IFCGEOMETRICREPRESENTATIONSUBCONTEXT(IFCGEOMETRICREPRESENTATIONCONTEXT):
	def __init__(self, ParentContext, TargetScale, TargetView, UserDefinedTargetView):
		 self.ParentContext = ParentContext
		 self.TargetScale = TargetScale
		 self.TargetView = TargetView
		 self.UserDefinedTargetView = UserDefinedTargetView