#!/usr/bin/python

import ConfigParser
import AuroraAlarm
import datetime

class settings(object):
	def __init__(self):
		self.config = ConfigParser.ConfigParser()
		self.config.read("Settings.cfg")
		self.test_mode = False
	
	def get_dawn_duration(self):
		duration_hour = int(self.config.get('DawnDuration', 'hour'))
		duration_minute = int(self.config.get('DawnDuration', 'minute'))
		duration = datetime.timedelta(hours=duration_hour, minutes=duration_minute)
		return duration

	def get_shutoff_delay(self):
		shutoff_hour = int(self.config.get('ShutoffDelay', 'hour'))
		shutoff_minute = int(self.config.get('ShutoffDelay', 'minute'))
		shutoff_duration = datetime.timedelta(hours=shutoff_hour, minutes=shutoff_minute)
		return shutoff_duration
	
	def get_alarms(self):
		# Read alarms from settings
		monday_hour = self.config.get('Monday', 'hour')
		monday_minute = self.config.get('Monday', 'minute')		
		monday_alarm = AuroraAlarm.Alarm(monday_hour, monday_minute, False)
		
		# Get datetime objects from alarms
		monday_alarm = monday_alarm.alarm_datetime
		tuesday_alarm = monday_alarm
		wednesday_alarm = monday_alarm
		thursday_alarm = monday_alarm
		friday_alarm = monday_alarm
		saturday_alarm = monday_alarm
		sunday_alarm = monday_alarm
		
		return {
			'Monday' : monday_alarm, 
			'Tuesday' : tuesday_alarm, 
			'Wednesday' : wednesday_alarm, 
			'Thursday' : thursday_alarm, 
			'Friday' : friday_alarm, 
			'Saturday' : saturday_alarm, 
			'Sunday' : sunday_alarm
		}
		
	def get_alarm(self, day):
		alarm_hour = self.config.get(day, 'hour')
		alarm_minute = self.config.get(day, 'minute')		

		alarm = self.parse_time(alarm_hour, alarm_minute)
		
# 		alarm = AuroraAlarm.Alarm(alarm_hour, alarm_minute, False)
		
		return alarm

	def parse_time(self, hour, minute):
		if(self.test_mode):
			print 'test mode!'
#			dawn_duration = datetime.timedelta(hours=1, minutes=0, seconds=0)
 			dawn_duration = datetime.timedelta(hours=0, minutes=30, seconds=0)
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
		
	def set_time(self, time):
		now = datetime.datetime.now()
		return datetime.datetime(now.year, now.month, now.day, time['hour'], time['minute'], time['second'])		

	def parse_hour(self, hour):
		return int(hour)

	def parse_minute(self, minute):
		return int(minute)

