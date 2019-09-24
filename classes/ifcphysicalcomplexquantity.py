class IFCPHYSICALCOMPLEXQUANTITY(IFCPHYSICALQUANTITY):
	def __init__(self, HasQuantities, Discrimination, Quality, Usage):
		 self.HasQuantities = HasQuantities
		 self.Discrimination = Discrimination
		 self.Quality = Quality
		 self.Usage = Usage