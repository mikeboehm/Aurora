#!/usr/bin/python

import datetime, threading, time
from Lights import Lights

# Glossary
# Dawn 		is the first appearance of light in the sky before sunrise. The start of the first sequence (black to red)
# Twilight 	is the period between dawn and sunrise
# Sunrise 	is the time in the morning when the sun appears. The start of the second sequence (red to white)
# Day 		occurs once the sunrise sequence is complete
# Daybreak 	could be the term for the event at the end of sunrise?


class Aurora(object):
	def __init__(self):
		self.lights = Lights()
		self.next_alarm = False
		self.keep_running = True
		# Update settings
# 		self.settings = self.get_settings()
		
		# Initialise alarm threads so we can test if they're running
		self.dawn_timer = threading.Timer(1, self.trigger_dawn)
		self.sunrise_timer = threading.Timer(1, self.trigger_sunrise)
		self.shutoff_thread = threading.Timer(1, self.trigger_autoshutoff)		
	
	# Returns settings from config
	def get_settings(self):
		# Set next update thread
		pass

	# Creates a Timer thread for the next alarm	
	def set_alarm(self):
		# Get next alarm
		next_alarm = self.get_next_alarm()
		
		dawn = next_alarm['dawn']['end_time'] - next_alarm['dawn']['duration']
		seconds_to_alarm = self.seconds_till_alarm(dawn)
		print 'Seconds till dawn: ', seconds_to_alarm
		
		self.dawn_timer = threading.Timer(seconds_to_alarm, self.trigger_dawn)
		self.dawn_timer.start()
# 		self.threads['dawn'] = dawn
		self.next_alarm = next_alarm
	
	# Setup dawn tranistion
	# Create a thread for sunrise
	def trigger_dawn(self):
		print 'trigger_dawn'
		# Fade
		end_colour = {'red': 4095, 'green': 0, 'blue': 0}
		duration = datetime.timedelta(seconds = 5)

		fade = {'end_colour': end_colour, 'duration': duration}
		self.lights.set_fade(fade)
		
		sunrise = self.next_alarm['sunrise']['end_time'] - self.next_alarm['sunrise']['duration']
		seconds_to_sunrise = self.seconds_till_alarm(sunrise)
		print 'Seconds till sunrise: ', seconds_to_sunrise
		self.sunrise_timer = threading.Timer(seconds_to_sunrise, self.trigger_sunrise)
		self.sunrise_timer.start()
# 		time.sleep(10)
		
	# Setup sunrise tranistion
	# Create a thread for day
	def trigger_sunrise(self):
		print 'trigger_sunrise'

		end_colour = {'red': 4095, 'green': 4095, 'blue': 4095}
		duration = datetime.timedelta(seconds = 10)
		fade = {'end_colour': end_colour, 'duration': duration}
		self.lights.set_fade(fade)

		# Setup auto-shutoff
		self.shutoff_thread = threading.Timer(15, self.trigger_autoshutoff)
		self.shutoff_thread.start()

	# Execute day routine (shut lights off)
	def trigger_autoshutoff(self):
		print 'turning lights off'
		end_colour = {'red': 0, 'green': 0, 'blue': 0}
		duration = datetime.timedelta(seconds = 2)
		fade = {'end_colour': end_colour, 'duration': duration}
		self.lights.set_fade(fade)
		
		# Set tomorrow's alarm
		# @todo implement
 		self.set_alarm() # Dawn triggers again, but it adds more and more delay each time
	
	# Returns the number of seconds until an event
	def seconds_till_alarm(self, end_time, start_time = False):
		if not start_time:
			print '!start_time'
			start_time = datetime.datetime.now()
			
		print 'End_time:', end_time
 		countdown_to_alarm = end_time - start_time
		return countdown_to_alarm.total_seconds()
	

	# Gets next alarm (typically tomorrow's)
	def get_next_alarm(self):
		# @todo Implement this properly
		duration = datetime.timedelta(seconds=10)
		now = datetime.datetime.now()		
		sunrise_end = now + datetime.timedelta(seconds=21)
		dawn_end = sunrise_end - duration
		day_ends = sunrise_end + duration

# 		print '@' * 20
# 		print 'Now:', now
# 		print 'Sunrise end:', sunrise_end
# 		print 'Dawn end:', dawn_end
# 		print 'Duration:', duration
		
		print now, sunrise_end, dawn_end, duration
		
		dawn = {'end_time': dawn_end, 'duration': duration}
		sunrise = {'end_time': sunrise_end, 'duration': duration}		
		day = {'end_time': day_ends}
		
# 		print dawn
# 		print sunrise
# 		print day
		
		return {'dawn': dawn, 'sunrise': sunrise, 'day': day}

	# Cleans up all running threads
	def shutdown(self):
		self.lights.lights_off()
		self.keep_running = False
		self.dawn_timer.cancel()
		self.sunrise_timer.cancel()
		self.shutoff_thread.cancel()

