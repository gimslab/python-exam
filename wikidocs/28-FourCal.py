class FourCal:
	def setdata(self, a, b):
		self.a=a
		self.b=b
	def sum(self):
		return self.a+self.b
	def mul(self):
		return self.a*self.b

c = FourCal()
c.setdata(2, 3)

print(c.sum())

print(c.mul())

