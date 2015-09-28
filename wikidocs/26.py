f = open("26-test.file", "w")

for i in range(1, 11):
	data = "%d 's line \n" % i
	f.write(data)

f.close()
