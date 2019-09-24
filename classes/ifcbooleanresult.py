class IFCBOOLEANRESULT(IFCGEOMETRICREPRESENTATIONITEM):
	def __init__(self, Operator, FirstOperand, SecondOperand):
		 self.Operator = Operator
		 self.FirstOperand = FirstOperand
		 self.SecondOperand = SecondOperand