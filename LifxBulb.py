import socket, colorsys
class LifxBulb(object):
	url = ''
	PORT = '56780'

	def __init__(self, JsonClient):
		self.JsonClient = JsonClient
		
		self.hostname = self.get_hostname()
	
	   
	def get_lights(self):
		path = '/lights'
		method = 'GET'
		
		return self.get(path)
		
	def get(self, path):
		url = "http://%s:%d%s" % (self.hostname, self.PORT, path)				 
		try:
			json = self.JsonClient.get(url)
		except IOError:
			settings = False
		return json
	
	def rgb_to_hsv(self, rgb):
		hsv = colorsys.rgb_to_hsv(rgb['red'], rgb['green'], rgb['blue'])
		print 'o' * 20
		print hsv
		return {
			'hue': hsv[1],
			'brightness': hsv[1],
			'saturation': hsv[2],			
		}
	
# 	def 
# 		curl -XPUT http://localhost:56780/lights/all/color -H "Content-Type: application/json" -d '{"hue": 120, "saturation": 1, "brightness": 1, "duration":2}'
		
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