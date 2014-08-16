import time
import datetime
import math
from threading import Thread

class Lights(object):
	def __init__(self):
		self.current_colour = {'red': 0, 'green': 0, 'blue': 0}
		
	def set_fade(self, fade):
		# Do fade calcs
		# Set fade calcs
		# Start fade_loop
		pass
		
	# Set threaded fade
	def set_fade(self, fade):
		duration = fade['duration']
		end_colour = fade['end_colour']
			
		self.fade_end_time = datetime.datetime.now() + duration
		self.fade_end_colour = end_colour
		# Get current light colour
		current_colour = self.get_lights()

		# Get colours differences
		self.fade_diffs_dict = self.fade_diffs(current_colour, end_colour)

		# Convert seconds into microsecnds
		total_duration = duration.seconds * 1000000
		self.fade_total_duration = float(total_duration)
		
		# Start fade loop
		fade_loop = Thread(target=self.fade_loop)
		fade_loop.start()
		
		
	def fade_loop(self):
		print 'Fade loop'
		# While now is <= fade end
			# Fade
		while datetime.datetime.now() <= self.fade_end_time:
			# time till end = end_time - now
			diff = self.fade_end_time - datetime.datetime.now()
			remaining = (diff.seconds * 1000000) + diff.microseconds
			percent_remaining = round((remaining/self.fade_total_duration) * 100,2)

			colour = self.fade_colours(self.fade_diffs_dict, percent_remaining)
			self.set_lights(colour)
		
			time.sleep(0.1)

		self.set_lights(self.fade_end_colour)

	def set_lights(self, colour):
		red = int(colour['red'])
		green = int(colour['green'])
		blue = int(colour['blue'])
		
		print 'red: ', red, 'green: ', green, 'blue: ', blue
		
		self.colour = {'red': red, 'green': green, 'blue': blue}
		
	def get_lights(self):
		return self.current_colour		

	# Returns a dict of the difference between two colours
	def fade_diffs(self, start_colour, end_colour):
		diff_red = self.fade_diff(end_colour['red'], start_colour['red'])
		diff_green = self.fade_diff(end_colour['green'], start_colour['green'])
		diff_blue = self.fade_diff(end_colour['blue'], start_colour['blue'])

		return {'red': diff_red, 'green': diff_green, 'blue': diff_blue}

	# Calculate the difference between two tints
	def fade_diff(self, start_colour, end_colour):
		diff = (end_colour - start_colour) / 100.00
		diff_absolute = math.fabs(diff)

		return { 'diff': diff, 'absolute': diff_absolute }
		

	# Returns colour to be set, based on the colour diffs
	def fade_colours(self, diffs, percent_remaining):
		# Calculate values
		red = self.fade_colour(diffs['red'], percent_remaining)
		green = self.fade_colour(diffs['green'], percent_remaining)
		blue = self.fade_colour(diffs['blue'], percent_remaining)

		return {'red': red, 'green': green, 'blue': blue}

	# Child method of fade_colours()
	def fade_colour(self, colour, percent_remaining):
		if(colour['diff'] < 0):
			colour_to_set = (100 - percent_remaining) * colour['absolute']
		else:
			colour_to_set = percent_remaining * colour['absolute']

		return colour_to_set
