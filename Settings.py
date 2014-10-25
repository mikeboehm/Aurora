import socket
from JsonClient import JsonClient

class Settings(object):
	def __init__(self, JsonClient):
		hostname = self.get_hostname()
		port = 5000
		path = '/get_settings'
		self.url = "http://%s:%d%s" % (hostname, port, path)
		self.JsonClient = JsonClient
		self.settings = self.refresh_settings()

	def get_settings(self):
		return self.settings

	def set_settings(self, settings):
		self.settings = settings

	def refresh_settings(self):
		settings = self.JsonClient.get(self.url)
		self.set_settings(settings)
		return settings

	def get_alarms(self):
		settings = self.get_settings()
		return settings['settings']['alarms']

	def get_alarm_for_day(self, day_number):
		alarms = self.get_alarms()
		day_number_string = str(day_number)
		
		alarm_string = alarms[day_number_string]['time']		
		alarm = alarm_string.split(':')
		
		hour = int(alarm[0])
		minutes = int(alarm[1])
		
		return {'hour': hour, 'minutes': minutes}
	
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