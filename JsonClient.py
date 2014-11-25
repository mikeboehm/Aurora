import urllib, json
class JsonClient(object):
	def get(self, url):
		response = urllib.urlopen(url);
		try:
			data = json.loads(response.read())
		except ValueError:
			import time
			time.sleep(2)
			data = json.loads(response.read())
		
		return data