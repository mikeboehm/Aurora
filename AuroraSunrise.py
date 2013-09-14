import datetime

# Handles sunrise/alarm
class Sunrise(object):
	def __init__(self):
		self.dawn_duration = datetime.timedelta(hours=1)
		self.shutoff_delay = datetime.timedelta(hours=1)
	
	# Returns the time of sunrise (full brightness)
	def sunrise(self):
		now = datetime.datetime.now()
		# monday_alarm = datetime.time(7,0,0)
		monday_alarm = datetime.datetime.now() + datetime.timedelta(hours=1, minutes=0, seconds=2)
		
# 		dawn_duration = datetime.timedelta(hours=1)
# 		shutoff_delay = datetime.timedelta(hours=1)
		
		today_alarm = datetime.datetime(now.year, now.month, now.day, monday_alarm.hour, monday_alarm.minute, monday_alarm.second)
#		shutoff = today_alarm + self.shutoff_delay
#		dawn_begin = today_alarm - self.dawn_duration
		# Get number of current day
		# Get sunrise for today
		
		return today_alarm
	
	# Returns the time of dawn (the start of the sequence)
	def dawn(self):
		return self.sunrise() - self.dawn_duration
	
	# Returns the time to shutoff the light after sunrise
	def shutoff(self):
		return self.sunrise() + self.shutoff_delay
		
	# Calculates what point in the sunrise we are at
	def stage(self):
		now = datetime.datetime.now()
		
		if now >= self.dawn() and now <= self.sunrise():
			print 'sun is rising'
		elif now > self.sunrise() and now <= self.shutoff():
			print 'sun has risen'
		elif now <= self.dawn():
			print 'still to come'
		else:
			print 'already happened'