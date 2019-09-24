# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:39:20 2018

@author: HEmam
"""
from ifcschemareader import IfcSchema
class CLSGenerator:
    
    def __init__(self, file):
        if file:
            self.schema = IfcSchema(file)
        
            for n in self.schema.entities:
                supertype= ""
                attributes = ""
                if n['supertype']:
                    supertype= n['supertype']
                if n['attributes']:
                    attributes = ", " + str([ str(x[0]) for x in n['attributes']])
                    attributes = attributes.replace("[","").replace("]","").replace("'","")
                f= open("./classes/"+ n['name'].lower()+ ".py","w+")
                f.write ("class " + n['name'] +"("+ supertype + "):\n")
                f.write ("\tdef __init__(self" + attributes + "):")
                if n['attributes']:
                    for x in n['attributes']:
                        f.write("\n\t\t self." + x[0] + " = " + x[0])
gen = CLSGenerator('IFC2X3_TC1.exp')