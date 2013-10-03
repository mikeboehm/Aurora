#!/usr/bin/python
import datetime

class Alarm(object):
	def __init__(self, hour, minute, test_mode = False):
		self.test_mode = test_mode
		time = self.parse_time(hour, minute)
		self.set_time(time)
		self.test_time()

	def parse_time(self, hour, minute):
		if(self.test_mode):
#			dawn_duration = datetime.timedelta(hours=1, minutes=0, seconds=0)
 			dawn_duration = datetime.timedelta(hours=0, minutes=2, seconds=0)
			now = datetime.datetime.now()
			alarm = datetime.datetime.now() + dawn_duration + datetime.timedelta(hours=0, minutes=0, seconds=2)
			hour = alarm.hour
			minute = alarm.minute
			second = alarm.second
		else:		
			hour = self.parse_hour(hour)
			minute = self.parse_minute(minute)
			second = 0

		return {'hour': hour, 'minute' : minute, 'second' : second}

	def parse_hour(self, hour):
		return int(hour)

	def parse_minute(self, minute):
		return int(minute)
		
	def set_time(self, time):
		now = datetime.datetime.now()
		self.hour = time['hour']
		self.minute = time['minute']
		self.alarm_datetime  = datetime.datetime(now.year, now.month, now.day, self.hour, self.minute, time['second'])		
	
	def test_time(self):
		hour = str(self.hour)
		minute = str(self.minute)
		print hour + ':' + minute