

class IfcOwnerHistory:

	def __init__(self, id, data):
		self.data = data
		values = data.split(",")
		self.OwningUser =  values[0].strip().replace("(","")
		self.OwningApplication =  values[1].strip()
		self.State =  values[2].strip()
		self.ChangeAction =  values[3].strip()
		self.LastModifiedDate =  values[4].strip()
		self.LastModifyingUser =  values[5].strip()
		self.LastModifyingApplication =  values[6].strip()
		self.CreationDate =  values[7].strip().replace(");","")
		
	
data = "(#3, #6, $, .ADDED., $, $, $, 1232965595);"
id = "#2"
owner = IfcOwnerHistory(id, data)
print(owner.OwningUser)