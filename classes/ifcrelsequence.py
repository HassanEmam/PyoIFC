class IFCRELSEQUENCE(IFCRELCONNECTS):
	def __init__(self, RelatingProcess, RelatedProcess, TimeLag, SequenceType):
		 self.RelatingProcess = RelatingProcess
		 self.RelatedProcess = RelatedProcess
		 self.TimeLag = TimeLag
		 self.SequenceType = SequenceType