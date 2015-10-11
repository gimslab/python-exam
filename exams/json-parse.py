import json

JSON_FILE="./json-parse-sample.json"
JSON={}

def readJsonFile(filename):
	f = open(filename, 'r')
	js = json.loads(f.read())
	f.close
	return js

print "__name__ = "+ __name__

def main():
	global JSON_FILE
	global JSON
	JSON = readJsonFile(JSON_FILE)

	repos = JSON['snapshot']['repos']
	userid = JSON['snapshot']['userid']
	pw = JSON['snapshot']['passwd']

	print "repos alue : "+repos
	print "userid value : " + userid
	print "pw value : "+pw

print "__name__ = "+ __name__

if __name__ == "__main__":
	main()
