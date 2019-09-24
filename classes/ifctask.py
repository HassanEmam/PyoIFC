class IFCTASK(IFCPROCESS):
	def __init__(self, TaskId, Status, WorkMethod, IsMilestone, Priority):
		 self.TaskId = TaskId
		 self.Status = Status
		 self.WorkMethod = WorkMethod
		 self.IsMilestone = IsMilestone
		 self.Priority = Priority