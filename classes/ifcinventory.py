class IFCINVENTORY(IFCGROUP):
	def __init__(self, InventoryType, Jurisdiction, ResponsiblePersons, LastUpdateDate, CurrentValue, OriginalValue):
		 self.InventoryType = InventoryType
		 self.Jurisdiction = Jurisdiction
		 self.ResponsiblePersons = ResponsiblePersons
		 self.LastUpdateDate = LastUpdateDate
		 self.CurrentValue = CurrentValue
		 self.OriginalValue = OriginalValue