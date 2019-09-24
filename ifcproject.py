import re

class IFCProject:

	def __init__(self, string):
	
		self.string = string
		self.id = self.getID()
		#self.GlobalId = self.getGlobalId()
		self.serialize()
		
	def getID(self):
		return self.string.split("=")[0]
		
	def getGlobalId(self):
		tmp = self.string.split("IfcProject('")[1]
		tmp = tmp.split("',")[0]
		return (tmp)
	
	def serialize(self):
		#tmp = self.string.split("IFCPROJECT")[1]
		tmp = self.string
		tmp = tmp.split(",")
		self.GlobalId = tmp[0].replace(" ","").replace("(","").replace("'","")
		self.OwnerHistory = tmp[1]
		self.Name = tmp[2].replace("'","")
		self.Description = tmp[3].replace("'","")
		self.ObjectType = tmp[4].replace("'","")
		self.LongName = tmp[5].replace("'","")
		self.Phase = tmp[6].replace("'","")
		self.RepresentationContexts = tmp[7].replace("'","").replace("(", "").replace(")","")
		self.UnitsInContext = tmp[8].replace("'","").replace(")","")
		
	def __str__(self):
		return (self.GlobalId + " " + self.OwnerHistory + 
		" " + self.Name + " " + self.Description + " " + self.ObjectType
		+ " " + self.LongName + " " +self.Phase+ " " + self.RepresentationContexts
		+ " " + self.UnitsInContext)
