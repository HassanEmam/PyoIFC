class IFCBSPLINECURVE(IFCBOUNDEDCURVE):
	def __init__(self, Degree, ControlPointsList, CurveForm, ClosedCurve, SelfIntersect):
		 self.Degree = Degree
		 self.ControlPointsList = ControlPointsList
		 self.CurveForm = CurveForm
		 self.ClosedCurve = ClosedCurve
		 self.SelfIntersect = SelfIntersect