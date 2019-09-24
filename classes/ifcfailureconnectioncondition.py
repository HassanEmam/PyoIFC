class IFCFAILURECONNECTIONCONDITION(IFCSTRUCTURALCONNECTIONCONDITION):
	def __init__(self, TensionFailureX, TensionFailureY, TensionFailureZ, CompressionFailureX, CompressionFailureY, CompressionFailureZ):
		 self.TensionFailureX = TensionFailureX
		 self.TensionFailureY = TensionFailureY
		 self.TensionFailureZ = TensionFailureZ
		 self.CompressionFailureX = CompressionFailureX
		 self.CompressionFailureY = CompressionFailureY
		 self.CompressionFailureZ = CompressionFailureZ