import datetime

# Handles sunrise/alarm
class Sunrise(object):
	def __init__(self):
		self.dawn_duration = datetime.timedelta(hours=1)
		self.shutoff_delay = datetime.timedelta(hours=1)
		self.update_time()

	# Updates the various time attributes
	def update_time(self):
		self.sunrise_time = self.sunrise()
		self.dawn_time = self.dawn()
		self.shutoff_time = self.shutoff()		
		
	# Returns the time of sunrise (full brightness)
	def sunrise(self):
		# Get number of current day
		# Get sunrise for today
		
		# Alarm is currently hardcoded so that dawn always begins in two seconds time for testing purposes
		now = datetime.datetime.now()
		monday_alarm = datetime.datetime.now() + self.dawn_duration + datetime.timedelta(hours=0, minutes=0, seconds=2)		
		today_alarm = datetime.datetime(now.year, now.month, now.day, monday_alarm.hour, monday_alarm.minute, monday_alarm.second)
		
		return today_alarm
	
	# Returns the time of dawn (the start of the sequence)
	def dawn(self):
		return self.sunrise_time - self.dawn_duration
	
	# Returns the time to shutoff the light after sunrise
	def shutoff(self):
		return self.sunrise_time + self.shutoff_delay
		
	# Calculates what point in the sunrise we are at
	def stage(self):
		now = datetime.datetime.now()
		if now >= self.dawn_time and now <= self.sunrise_time:
			print 'sun is rising'
		elif now > self.sunrise_time and now <= self.shutoff_time:
			print 'sun has risen'
		elif now <= self.dawn_time:
			print 'still to come'
		else:
			print 'already happened'