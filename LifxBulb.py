import socket, json, colorsys, urllib2
class LifxBulb(object):
	url = ''
	PORT = 56780

	def __init__(self, JsonClient):
		self.JsonClient = JsonClient
		
		self.hostname = self.get_hostname()
	
	
	def set_colour(self, colour):
		self.do_request('PUT', '/lights/all/color', colour)
# 		print 'msg:', response.msg
# 		print 'code:', response.code
# 		print 'headers:', response.headers
# 		print 'url:', response.url
	
	def do_request(self, request_type, path, body = None):
		if body:
			body = json.JSONEncoder().encode(body)

		url = "http://%s:%d%s" % (self.hostname, self.PORT, path)
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url, data=body)
		request.add_header('Content-Type', 'application/json')
		request.get_method = lambda: request_type
		response = opener.open(request)
	
	
	def get_lights(self):
		path = '/lights'
		method = 'GET'
		
		return self.get_url(path)

	def set_lights_on(self):
		path = '/lights/all/on'
		method = 'GET'
		
		return self.JsonClient.put(path)
			
	def get_url(self, path):
		url = "http://%s:%d%s" % (self.hostname, self.PORT, path)				 
		try:
			json = self.JsonClient.get(url)
		except IOError:
			settings = False
		return json
	
	def put(self, path):
		url = "http://%s:%d%s" % (self.hostname, self.PORT, path)				 

		PUT /lights/{selector}/on
	
	def get_hostname(self):
		# Generate hostname
		bonjour_address = socket.gethostname()
		# If IP address, use as is
		try:
			socket.inet_aton(bonjour_address)	
		except socket.error:
			# Otherwise make sure the address will work
			if not bonjour_address.endswith('.local'):
				bonjour_address += '.local'
		
		return bonjour_address