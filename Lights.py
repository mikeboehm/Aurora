import time
import datetime
import math
from threading import Thread

class Lights(object):
	def __init__(self):
		self.queue = {}
	
	def add_to_queue(self, from_time, duration, end_colour, start_colour = False):
		fade_event = {'from_time': from_time, 'duration': duration, 'end_colour' : end_colour}
		self.queue[] = fade_event
	
	def fade_loop(self):
		fade_event = self.queue.pop()
		if fade_event:
			self.fade(fade_event)
		
	# Execute light transition
	def fade(self, fade_event):
		from_time = fade_event['from_time']
		duration = fade_event['duration']
		end_colour = fade_event['end_colour']
		# Calculate time till end
		# Now + duration = end_time
		end_time = from_time + duration


		# Convert seconds into microsecnds
		total_duration = duration.seconds * 1000000
		total_duration = float(total_duration)

		print '=' * 10 + ' Start fade loop ' + '=' * 10
		start_time = time.time()
		while datetime.datetime.now() <= end_time:
			# time till end = end_time - now
			diff = end_time - datetime.datetime.now()
			remaining = (diff.seconds * 1000000) + diff.microseconds
			percent_remaining = round((remaining/total_duration) * 100,2)
			
			print percent_remaining

			time.sleep(0.1)

		end_time = time.time()
		print '=' * 10 + ' Elapsed ' + '=' * 10
		print end_time - start_time

# 		self.set_lights(end_colour)