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
		# Update settings
# 		self.settings = self.get_settings()

		# Get next alarm
		next_alarm = self.next_alarm()
		print next_alarm
		# Set alarm thread(s)
		self.set_alarm(next_alarm)
		# @todo Set button toggle callback
	
	# Returns settings from config
	def get_settings(self):
		# Set next update thread
		pass

	# Creates a Timer thread for the next alarm	
	def set_alarm(self, next_alarm):
		seconds_to_alarm = self.seconds_till_alarm(next_alarm['dawn']['end_time'])

		dawn = threading.Timer(seconds_to_alarm, self.trigger_dawn)
		dawn.start()
# 		self.threads['dawn'] = dawn
	
	# Setup dawn tranistion
	# Create a thread for sunrise
	def trigger_dawn(self):
		print 'trigger_dawn'
		# Fade
		end_colour = {'red': 4095, 'green': 0, 'blue': 0}
		duration = datetime.timedelta(seconds = 10)
# 		end_time = datetime.datetime.now() + duration
		fade = {'end_colour': end_colour, 'duration': duration}
		self.lights.set_fade(fade)
		
		#self.next_alarm['dawn']

# 	# Setup sunrise tranistion
# 	# Create a thread for day
# 	def trigger_sunrise(self):
# 		print 'trigger_sunrise'
# 		# Setup auto-shutoff
# 		shutoff = threading.Timer(2.0, self.trigger_autoshutoff)
# 		shutoff.start()
# 		self.threads['day'] = shutoff

# 	# Execute day routine (shut lights off)
# 	def trigger_autoshutoff(self):
# 		print 'turning lights off'
	
	# Returns the number of seconds until an event
	def seconds_till_alarm(self, end_time, start_time = datetime.datetime.now()):
 		countdown_to_alarm = end_time - start_time
		return countdown_to_alarm.total_seconds()
	

	# Gets next alarm (typically tomorrow's)
	def next_alarm(self):
		# @todo Implement this properly
		dawn_time = datetime.datetime.now() + datetime.timedelta(seconds=10)		
		duration = datetime.timedelta(seconds=10)
		end_colour = {'red': 255, 'green': 0, 'blue': 0}

		dawn = {'end_time': dawn_time, 'duration': duration, 'end_colour': end_colour}
		
		print dawn_time
		
		return {'dawn': dawn}

	# Cleans up all running threads
	def shutdown(self):
		pass
	
try:
	aurora = Aurora()
	# Main loop
# 	while True:
# 		print 'sleeping: ', datetime.datetime.now().time()
# 		time.sleep(10) # Remember that the set_alarm() returns almost instantly, so the sleep should probably be
# 		print 'set up:   ', datetime.datetime.now().time()
# 		aurora.set_alarm(aurora.next_alarm)

except KeyboardInterrupt:
	aurora.shutdown()
	print '#' * 10 + ' Exiting ' + '#' * 10
