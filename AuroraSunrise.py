#!/usr/bin/python

import datetime
import math
import AuroraSettings

# Handles sunrise/alarm
class Sunrise(object):
	def __init__(self):
		self.settings = AuroraSettings.settings()
		self.update_settings()
		self.today_alarm()
		self.update_times()		
	
	def update_settings(self):
		self.dawn_duration = self.settings.get_dawn_duration()
		self.shutoff_delay = self.settings.get_shutoff_delay()
		
		self.update_alarms()	
	
	def today_alarm(self):
		print '=' * 10 + ' today_alarm() ' + '=' * 10 
		now = datetime.datetime.now()
		self.today_alarm = self.get_alarm(now.isoweekday())
		print self.today_alarm
		return self.today_alarm
	
	def get_alarm(self, week_day_number):
		print '=' * 10 + ' get_alarm() ' + '=' * 10 
		print week_day_number
		days_of_the_week = { 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5: 'Friday', 6 : 'Saturday', 7 : 'Sunday'}
		return self.alarms[days_of_the_week[week_day_number]]		
	
	# Updates the various time attributes
	def update_times(self):
		print '=' * 10 + ' update_time() ' + '=' * 10 
		self.sunrise_time = self.sunrise()
		self.dawn_time = self.dawn()
		self.shutoff_time = self.shutoff()		
	
	def update_alarms(self):
		print '=' * 10 + ' update_alarms() ' + '=' * 10 
		self.alarms = self.settings.get_alarms()
		
	# Returns the time of sunrise (full brightness)
	def sunrise(self):
		print '=' * 10 + ' sunrise() ' + '=' * 10 
		# @todo Get number of current day
		# @todo Get sunrise for today
				
		# Alarm is currently hardcoded so that dawn always begins in two seconds time for testing purposes
		# @todo remove this once method is properly implemented
		now = datetime.datetime.now()
		today_name = now.strftime('%A')
# 		today_alarm = self.alarms[today_name]
		print today_name
		
		today_alarm = self.today_alarm
# 		monday_alarm = datetime.datetime.now() + self.dawn_duration + datetime.timedelta(hours=0, minutes=0, seconds=2)		
# 		today_alarm = datetime.datetime(now.year, now.month, now.day, monday_alarm.hour, monday_alarm.minute, monday_alarm.second)
		
		return today_alarm
	
	# Returns the time of dawn (the start of the sequence)
	def dawn(self):
		print '=' * 10 + ' dawn() ' + '=' * 10 
		return self.sunrise_time - self.dawn_duration
	
	# Returns the time to shutoff the light after sunrise
	def shutoff(self):
		print '=' * 10 + ' shutoff() ' + '=' * 10 
		return self.sunrise_time + self.shutoff_delay

	def progress(self, seconds_into_dawn):
		# As a percentage of progress (starts at 0)
		# 100 - (((3600-900)/3600)*100) = 25
		dawn_duration = self.dawn_duration.total_seconds()
		progress = 100 - (((dawn_duration - seconds_into_dawn) / dawn_duration) * 100)
		# Cap progress percentage so that it works with the shutoff delay as well
#		print round(progress, 2)
		if progress > 100:
			progress = 100
		return round(progress, 2)
		
	# Calculates what point in the sunrise we are at
	def stage(self):
# 		print '=' * 10 + ' stage() ' + '=' * 10 		
		now = datetime.datetime.now()
		diff = now - self.dawn_time
		seconds_into_dawn = math.floor(diff.total_seconds())

		# Dawn has begun
		if now >= self.dawn_time and now <= self.sunrise_time:			
			progress = self.progress(seconds_into_dawn)
# 			print 'sun is rising ' + str(progress)
		# The sun has risen
		elif now > self.sunrise_time and now <= self.shutoff_time:
			progress = self.progress(seconds_into_dawn)
			print 'sun has risen'
		# Dawn is coming
		elif now <= self.dawn_time:
			progress = 0
			print 'still to come'
		# Sunrise has been and gone
		else:
			progress = 0
			print 'already happened'
			
		return progress