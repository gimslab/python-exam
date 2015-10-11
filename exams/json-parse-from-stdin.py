import json
import sys


class JsonObject:
	def __init__(self, d):
		self.__dict__ = d

js = json.loads(sys.stdin.read(), object_hook=JsonObject)

print "js.repos = "+js.release.repos
print "js.userid = "+js.release.userid
print "js.passwd = "+js.release.passwd
print "js.arrTest = "+js.component.arrayTest[1]
print "js.arrTest2 = "+js.releaseHistory[1].release.userid
