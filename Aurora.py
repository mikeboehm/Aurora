#!/usr/bin/python

import datetime, threading, time
from Lights import Lights
import os
os.system('clear')

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
		# Update settings
# 		self.settings = self.get_settings()

		
		
		# Set alarm thread(s)
		
		# @todo Set button toggle callback
	
	# Returns settings from config
	def get_settings(self):
		# Set next update thread
		pass

	# Creates a Timer thread for the next alarm	
	def set_alarm(self):
		# Get next alarm
		self.next_alarm = self.get_next_alarm()
		
		dawn = self.next_alarm['dawn']['end_time'] - self.next_alarm['dawn']['duration']
		seconds_to_alarm = self.seconds_till_alarm(dawn)
		print 'Seconds till dawn: ', seconds_to_alarm
		
		dawn_timer = threading.Timer(seconds_to_alarm, self.trigger_dawn)
		dawn_timer.start()
# 		self.threads['dawn'] = dawn
	
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
		sunrise_timer = threading.Timer(seconds_to_sunrise, self.trigger_sunrise)
		sunrise_timer.start()
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
		shutoff_thread = threading.Timer(15, self.trigger_autoshutoff)
		shutoff_thread.start()

	# Execute day routine (shut lights off)
	def trigger_autoshutoff(self):
		print 'turning lights off'
		end_colour = {'red': 0, 'green': 0, 'blue': 0}
		duration = datetime.timedelta(seconds = 2)
		fade = {'end_colour': end_colour, 'duration': duration}
		self.lights.set_fade(fade)
		
		# Set tomorrow's alarm
		# @todo implement
	
	# Returns the number of seconds until an event
	def seconds_till_alarm(self, end_time, start_time = datetime.datetime.now()):
 		countdown_to_alarm = end_time - start_time
		return countdown_to_alarm.total_seconds()
	

	# Gets next alarm (typically tomorrow's)
	def get_next_alarm(self):
		# @todo Implement this properly
		duration = datetime.timedelta(seconds=10)
		sunrise_end = datetime.datetime.now() + datetime.timedelta(seconds=21)
		dawn_end = sunrise_end - duration
		day_ends = sunrise_end + duration

		print 'Sunrise end:', sunrise_end
		print 'Dawn end:', dawn_end
		
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

if __name__ == '__main__':
	try:
		aurora = Aurora()
		aurora.set_alarm()
		print 'already exited'
		time.sleep(10)
	# 	aurora.shutdown()
		# Main loop
	# 	while True:
	# 		print 'sleeping: ', datetime.datetime.now().time()
	# 		time.sleep(10) # Remember that the set_alarm() returns almost instantly, so the sleep should probably be
	# 		print 'set up:   ', datetime.datetime.now().time()
	# 		aurora.set_alarm(aurora.next_alarm)
	
	except KeyboardInterrupt:
		aurora.shutdown()
		print '#' * 10 + ' Exiting ' + '#' * 10
