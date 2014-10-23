#!/usr/bin/python

import datetime, threading, time
import pika
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
		
		self.rabbit_listener_thread = threading.Thread(target=self.rabbit_listner)
		self.rabbit_listener_thread.start()

	def rabbit_listner(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))
		channel = connection.channel()
		
		channel.queue_declare(queue='hello')
		
		print ' [*] Waiting for messages. To exit press CTRL+C'
		
		
		channel.basic_consume(self.rabbit_callback,
			queue='hello',
			no_ack=True)
		
		channel.start_consuming()

	

	def rabbit_callback(self, ch, method, properties, body):
	    print " [x] Received %r" % (body,)
	    self.lights.toggle_lights()

		
	
	# Returns settings from config
	def get_settings(self):
		# Set next update thread
		pass

	# Creates a Timer thread for the next alarm	
	def set_alarm(self):
		# Get next alarm
		next_alarm = self.get_next_alarm()
		print 'Sunrise:', next_alarm['sunrise']['end_time']		
		
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
		# @todo Put colour into config file
		end_colour = {'red': 4095, 'green': 0, 'blue': 0}
# 		duration = datetime.timedelta(seconds = 5)
		duration = self.next_alarm['dawn']['duration']

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
		
		# @todo Put colour into config file
		end_colour = {'red': 4095, 'green': 4095, 'blue': 4095}
# 		duration = datetime.timedelta(seconds = 10)
		duration = self.next_alarm['sunrise']['duration']
		fade = {'end_colour': end_colour, 'duration': duration}
		self.lights.set_fade(fade)

		# Setup auto-shutoff
		day_ends = self.next_alarm['day']['end_time']
		seconds_of_day = self.seconds_till_alarm(day_ends)
		print 'seconds_of_day', seconds_of_day
		self.shutoff_thread = threading.Timer(seconds_of_day, self.trigger_autoshutoff)
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
			start_time = datetime.datetime.now()
			
 		countdown_to_alarm = end_time - start_time
		return countdown_to_alarm.total_seconds()
	
	# Returns alarm for day of the week
	# 0 is Sunday
	# 1 Monday
	# 2	Tuesday
	# 3	Wednesday
	# 4	Thursday
	# 5	Friday
	# 6	Saturday	
	def get_alarm_for_day_number(self, day_number):
		day_number = int(day_number)
		if day_number > 6:
			day_number = 0
		now = datetime.datetime.now()		
		today_number = int(now.strftime("%w"))		
								
		# @todo read from config file instead
		# Weekend
		if(day_number == 0 or day_number == 6) :
			hour = 9
			minutes = 30
		else :
			hour = 6
			minutes = 45
		
		alarm_day = now
		# Calculate date based on difference between day numbers
		increment = datetime.timedelta(days=1)
		# Keep adding days until the alarm day number is the same as the parameter day number
		while int(alarm_day.strftime("%w")) is not day_number:
			alarm_day += increment
				
		dawn_duration = datetime.timedelta(minutes=15)
		sunrise_duration = datetime.timedelta(minutes=15)
		auto_shutoff_delay = datetime.timedelta(minutes=60)

		year = alarm_day.strftime("%Y")
		month = alarm_day.strftime("%m")
		day = alarm_day.strftime("%d")

		sunrise_end = datetime.datetime(int(year),int(month),int(day), int(hour), int(minutes))
		dawn_end = sunrise_end - sunrise_duration
		day_ends = sunrise_end + auto_shutoff_delay
						
		dawn = {'end_time': dawn_end, 'duration': dawn_duration}
		sunrise = {'end_time': sunrise_end, 'duration': sunrise_duration}		
		day = {'end_time': day_ends}
				
		return {'dawn': dawn, 'sunrise': sunrise, 'day': day}	
	
	def get_today_alarm(self):
		now = datetime.datetime.now()		
		day_number = now.strftime("%w")
		
		today_alarm = self.get_alarm_for_day_number(day_number)
		
		return today_alarm

	
	# Gets next alarm (typically tomorrow's)
	def get_next_alarm(self):
		now = datetime.datetime.now()
		today_alarm = self.get_today_alarm()
		
		if (now >= today_alarm['sunrise']['end_time']):
			print "now >= today_alarm['sunrise']['end_time'])"
			day_number = int(now.strftime("%w"))
			next_alarm = self.get_alarm_for_day_number(day_number + 1)
		else :			
			print now, today_alarm['sunrise']['end_time']
			next_alarm = today_alarm
		
		# Demo mode ######################
# 		dawn_duration = datetime.timedelta(minutes=1)
# 		sunrise_duration = datetime.timedelta(minutes=1)
# 		auto_shutoff_delay = datetime.timedelta(minutes=1)
# 		
# 		sunrise_delay = dawn_duration + sunrise_duration + datetime.timedelta(seconds=5)
# 		
# 		sunrise_end = datetime.datetime.now() + sunrise_delay
# 		dawn_end = sunrise_end - sunrise_duration
# 		day_ends = sunrise_end + auto_shutoff_delay
# 						
# 		dawn = {'end_time': dawn_end, 'duration': dawn_duration}
# 		sunrise = {'end_time': sunrise_end, 'duration': sunrise_duration}		
# 		day = {'end_time': day_ends}
# 		return {'dawn': dawn, 'sunrise': sunrise, 'day': day}
		
		# END DEMO MODE ##################
		
		return next_alarm

	# Cleans up all running threads
	def shutdown(self):
		self.lights.lights_off()
		self.keep_running = False
		self.dawn_timer.cancel()
		self.sunrise_timer.cancel()
		self.shutoff_thread.cancel()
		self.rabbit_listener_thread.join()
# 		self.lights.shutdown()

