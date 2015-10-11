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


class FourCal2(FourCal):
	def sub(self):
		return self.a - self.b
	def div(self):
		return self.a / self.b


c2 = FourCal2()
c2.setdata(12, 3)
print("%s - %s = %s" % (c2.a, c2.b, c2.sub()))
print("%s / %s = %s" % (c2.a, c2.b, c2.div()))
