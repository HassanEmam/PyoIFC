class IFCPOSTALADDRESS(IFCADDRESS):
	def __init__(self, InternalLocation, AddressLines, PostalBox, Town, Region, PostalCode, Country):
		 self.InternalLocation = InternalLocation
		 self.AddressLines = AddressLines
		 self.PostalBox = PostalBox
		 self.Town = Town
		 self.Region = Region
		 self.PostalCode = PostalCode
		 self.Country = Country