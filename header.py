import re

find = re.compile("(.*?)\((.*?)\);")

class Header:

	def __init__(self, lines):
		attributes = []
		for line in lines:
			if find.search(line):
				attributes = find.search(line).groups()
				if attributes[0].strip() == "FILE_DESCRIPTION":
					self.parseDescription(attributes[1].strip(","))
				elif attributes[0].strip() == "FILE_NAME":
					print("File Name:")
					self.parseFileName(attributes[1].strip())
				elif attributes[0].strip() == "FILE_SCHEMA":
					self.parseSchema(attributes[1].strip().replace("('", "").replace("')",""))
	
	def parseDescription(self, description):
		values = description.split(",")
		print(values)
		self.description = values[0].replace("('","").replace("')","")
		self.version = values[1].replace("'","").strip()

	def parseSchema(self, schema):
		self.Schema = schema
		
	def parseFileName(self, filename):
		values = filename.split(",")
		self.name = values[0].strip()
		self.time_stamp = values[1].strip()
		self.author = values[2].strip()
		self.organization = values[3].strip()
		self.preprocesspr_version = values[4].strip()
		self.ongoing_system = values[5].strip()
		self.authorization = values[6].strip()
		
	def __str__(self):
		return ("{Description: " + self.description
		+ ", name: " + self.name
		+ "}")
			

line =[]
line.append("FILE_DESCRIPTION (('ViewDefinition [CoordinationView]'), '2;1');")
line.append("FILE_NAME ('example.ifc', '2009-01-26T11:26:35', ('Architect'), ('Building Designer Office'), 'IFC Engine DLL version 1.02 beta', 'IFC Engine DLL version 1.02 beta', 'The authorising person');")
line.append("FILE_SCHEMA (('IFC2X3'));")
header= Header(line)
