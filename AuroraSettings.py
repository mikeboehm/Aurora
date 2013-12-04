#!/usr/bin/python

import ConfigParser
import AuroraAlarm
import datetime

class settings(object):
	def __init__(self):
		self.config = ConfigParser.ConfigParser()
		self.config.read("Settings.cfg")
	
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
		monday_alarm = AuroraAlarm.Alarm(monday_hour, monday_minute, True)
		
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