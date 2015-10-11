import json

JSON_FILE="./json-parse-sample.json"


class JsonObject:
	def __init__(self, d):
		self.__dict__ = d

f = open(JSON_FILE, 'r')
js = json.loads(f.read(), object_hook=JsonObject)
f.close

print "js.repos = "+js.release.repos
print "js.userid = "+js.release.userid
print "js.passwd = "+js.release.passwd
print "js.arrTest = "+js.component.arrayTest[1]
print "js.arrTest2 = "+js.releaseHistory[1].release.userid
