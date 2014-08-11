#!/usr/bin/python

import datetime, threading, time
import os
os.system('clear')

# Dawn is the first appearance of light in the sky before sunrise
# So dawn is the start of the first sequence
# Twilight is the period between dawn and sunrise
# Sunrise is the time in the morning when the sun appears
# So sunrise is the start of the second sequence
# Day occurs once the sunrise sequence is complete
# Daybreak could be the term for the event at the end of sunrise?


class Aurora(object):
	def __init__(self):
		self.threads = {}
		self.next_alarm = self.next_alarm()
		self.alarm = self.set_alarms(self.next_alarm)
		print self.next_alarm
		# Set button toggle callback ?
		# Update
			# Set next update thread
		# Get next alarm
			# Set alarm thread(s)
				# Set dawn thread
				# Set sunrise thread
				# Set daylight shutoff thread
	
	# Setup dawn tranistion
	# Create a thread for sunrise
	def trigger_dawn(self):
		print 'trigger_dawn'
		# Setup sunrise
		sunrise = threading.Timer(2.0, self.trigger_sunrise)
		sunrise.start()
		self.threads['sunrise'] = sunrise

	# Setup sunrise tranistion
	# Create a thread for day
	def trigger_sunrise(self):
		print 'trigger_sunrise'
		# Setup auto-shutoff
		shutoff = threading.Timer(2.0, self.trigger_autoshutoff)
		shutoff.start()
		self.threads['day'] = shutoff

	# Execute day routine (shut lights off)
	def trigger_autoshutoff(self):
		print 'turning lights off'
	
	# Creates a Timer thread for the next alarm	
	def set_alarms(self, next_alarm):
		dawn = threading.Timer(2.0, self.trigger_dawn)
		dawn.start()
		self.threads['dawn'] = dawn

	# Gets next alarm (typically tomorrow's)
	def next_alarm(self):
		next_alarm = datetime.datetime.now() + datetime.timedelta(minutes=10)
		return next_alarm

	# Cleans up all running threads
	def shutdown(self):
		pass
	
try:
	aurora = Aurora()
	# Main loop
	while True:
		print 'sleeping: ', datetime.datetime.now().time()
		time.sleep(10) # Remember that the set_alarms() returns almost instantly, so the sleep should probably be
		print 'set up:   ', datetime.datetime.now().time()
		aurora.set_alarms(aurora.next_alarm)

except KeyboardInterrupt:
	aurora.shutdown()
	print '#' * 10 + ' Exiting ' + '#' * 10
