#!/usr/bin/python

import datetime
import os
# import TodayAlarm
os.system('clear')

class TodayAlarm(object):
	def __init__(self):
		today = datetime.date.today()
		self.day_number = today.isoweekday()
		
		now = datetime.datetime.now()
		# monday_alarm = datetime.time(7,0,0)
		monday_alarm = datetime.datetime.now() + datetime.timedelta(hours=1, minutes=0, seconds=2)
		dawn_duration = datetime.timedelta(hours=1)
		shutoff_delay = datetime.timedelta(hours=1)
		
		today_alarm = datetime.datetime(now.year, now.month, now.day, monday_alarm.hour, monday_alarm.minute, monday_alarm.second)
		shutoff = today_alarm + shutoff_delay
		dawn_begin = today_alarm - dawn_duration
		
		self.sunrise = today_alarm
		self.shutoff = shutoff
		self.dawn = dawn_begin

class Lights(object):
	
	
today_alarm = TodayAlarm()
print today_alarm.dawn_begin
print today_alarm.today_alarm
print today_alarm.shutoff

