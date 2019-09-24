class IFCWORKCONTROL(IFCCONTROL):
	def __init__(self, Identifier, CreationDate, Creators, Purpose, Duration, TotalFloat, StartTime, FinishTime, WorkControlType, UserDefinedControlType):
		 self.Identifier = Identifier
		 self.CreationDate = CreationDate
		 self.Creators = Creators
		 self.Purpose = Purpose
		 self.Duration = Duration
		 self.TotalFloat = TotalFloat
		 self.StartTime = StartTime
		 self.FinishTime = FinishTime
		 self.WorkControlType = WorkControlType
		 self.UserDefinedControlType = UserDefinedControlType