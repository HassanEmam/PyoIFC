from header import Header
import json
from ifcproject import IFCProject
import re

regex = re.compile("#(\d+)[ ]?=[ ]?(.*?)\((.*)\);[\\r]?$")

class IFCParser:
	def __init__(self, file): 
		header = False
		headers =[]
		data = False
		self.data_dic = {}
		with open(file) as fp:  
			line = fp.readline()
			cnt = 1
			print("Line: {}".format(line.strip()))
			while line:
				if line.strip() == "HEADER;":
					header = True
				elif line.strip() =="ENDSEC;":
					header = False
				elif line.strip() == "DATA;":
					data = True
				elif header == True:
					print("Header {}: {}".format(cnt, line.strip()))
					headers.append(line.strip())
				elif data:
					#print("Data {}: {}".format(cnt, line.strip()))
					res = regex.search(line.strip())
					attrs = ""
					name = "" 
					id = "" 
					if res:
						id, name, attrs = res.groups()
						info = {}
						info["IFC_Type"] = name
						info['attrs'] = attrs
						self.data_dic['#'+id] = info
					# if name.lower() == "ifcproject":
					# 	self.project = IFCProject(line.strip())
						#print("Project Printing: " + str(self.project))
				line = fp.readline()
				
				cnt += 1
				
		#print(headers)
		self.header = Header(headers)
f = IFCParser('test.ifc')
print(f.header)

for k in f.data_dic:
	print(k , f.data_dic[k]['IFC_Type'])
	if f.data_dic[k]['IFC_Type'] == 'IFCPROJECT':
		project = IFCProject(f.data_dic[k]['attrs'])
		print('Project', project)
print('f\t', f.data_dic)