from Adafruit_PWM_Servo_Driver import PWM
import time
import datetime
import math
class Lights(object):
	def __init__(self):
		self.pwm = PWM(0x40, debug=True)
		self.freq = 10
		self.pwm.setPWMFreq(self.freq)
		self.red_pin = 1
		self.green_pin = 2
		self.blue_pin = 3

		self.light_state = False
		self.reading_light = {'red': 255, 'green': 255, 'blue': 255}
		self.reading_light['red'] = self.reading_light['red'] * 16
		self.reading_light['green'] = self.reading_light['green'] * 16
		self.reading_light['blue'] = self.reading_light['blue'] * 16
		print 'red: ' + str(self.reading_light['red'])
		
		self.colour = {'red': 0, 'green': 0, 'blue': 0}
		
		self.pwm.setPWM(self.red_pin, 0 , 0)
		self.pwm.setPWM(self.green_pin, 0, 0)
		self.pwm.setPWM(self.blue_pin, 0, 0)

	def toggle_light_callback(self, channel):
		print 'toggle_light_callback'
# 		self.pwm.setPWM(self.green_pin, 0 , 2000)
# 		time.sleep(0.1)
# 		self.pwm.setPWM(self.green_pin, 0 , 0)
		self.toggle_light(channel)

	# Turns the reading light on and off
	def toggle_light(self, channel):
		print 'toggle_light'
		start_time = time.time()
		duration = datetime.timedelta(seconds=1)
# 		print self.light_state
		if self.light_state:
 			self.toggle_light_off(duration)
			print "turning off"
		else:
			self.toggle_light_on(duration)
			print "turning on"
		elapsed_time = time.time() - start_time
		print elapsed_time


	# Turns reading light on
	def toggle_light_on(self, duration):
		print 'toggle_light_on'
		print self.reading_light['red']
		now = datetime.datetime.now()
		self.fade(now, duration, self.reading_light)

# 		print x
# 		print 'red: ' + str(red)
		self.light_state = True
# 		time.sleep(1)

	# Turns reading light off
	def toggle_light_off(self, duration):
		print 'toggle_light_off'
		print duration
		from_time = datetime.datetime.now()
		end_colour = {'red': 0, 'green': 0, 'blue': 0}
		self.fade(from_time, duration, end_colour)

		self.light_state = False

	# Sets the light relative to where we are in the sequence
	def set_sunrise_colour(self, progress):
		if self.light_state == False:
			if progress <= 50:
				colour = self.phase_one(progress)
			else:
				colour = self.phase_two(progress)

			self.set_lights(colour)

	def test(self):
		print 'Aurora Lights!'

	# Black to Red
	def phase_one(self, progress):
# 		print '=' * 10 + ' phase_one() ' + '=' * 10
		# rgb(255,0,0)

		# Factor in that progress within phase_one() will only go as high as 50
		progress = (progress / 50) * 100

		red = float(4095)/100 # calculate 1% of max red
		red *= progress # translate that to current progress
		green = 0
		blue = 0

		colour = {'red': red, 'green': green, 'blue': blue}

		return colour

	# Red to white
	def phase_two(self, progress):
# 		print '=' * 10 + ' phase_two() ' + '=' * 10
		# rgb(255,255,255)
		# Factor in that progress within phase_two() will start at >50
		progress = (progress - 50) * 2

		red = 4095
		green = (float(4095)/100)* progress
		blue = (float(4095)/100)* progress

		colour = {'red': red, 'green': green, 'blue': blue}

		return colour

	def set_lights(self, colour):
		red = int(colour['red'])
		green = int(colour['green'])
		blue = int(colour['blue'])

		# Prevent out of range
		if(red > 4095):
			red = 4095
		if(green > 4095):
			green = 4095
		if(blue > 4095):
			blue = 4095

		# Prevent out of range
		if(red < 0):
			red = 0
		if(green < 0):
			green = 0
		if(blue < 0):
			blue = 0

# 		print 'R:' + str(red) + ', G:' + str(green) + ', B:' + str(blue)
		self.pwm.setPWM(self.red_pin, 0 , red)
		self.pwm.setPWM(self.green_pin, 0, green)
		self.pwm.setPWM(self.blue_pin, 0, blue)
		
		self.colour = {'red': red, 'green': green, 'blue': blue}
	
	def turn_off(self):
		colour = {'red': 0, 'green': 0, 'blue': 0}
		self.set_lights(colour)
	
	def get_lights(self):
		return self.colour
	
	def fade_diff(self, start_colour, end_color):
		diff = (end_color - start_colour) / 100.00	
		diff_absolute = math.fabs(diff)
		
		return { 'diff': diff, 'absolute': diff_absolute }
	
	def fade_colour(self, colour, percent_remaining):
		if(colour['diff'] < 0):
			colour_to_set = (100 - percent_remaining) * colour['absolute']
		else:				
			colour_to_set = percent_remaining * colour['absolute']
			
		return colour_to_set
	
	def fade_colours(self, diffs, percent_remaining):
		# Calculate values
		red = self.fade_colour(diffs['red'], percent_remaining)
		green = self.fade_colour(diffs['green'], percent_remaining)
		blue = self.fade_colour(diffs['blue'], percent_remaining)
		
		return {'red': red, 'green': green, 'blue': blue}
	

	def fade_diffs(self, start_colour, end_colour):
		diff_red = self.fade_diff(end_colour['red'], start_colour['red'])
		diff_green = self.fade_diff(end_colour['green'], start_colour['green'])
		diff_blue = self.fade_diff(end_colour['blue'], start_colour['blue'])
		
		return {'red': diff_red, 'green': diff_green, 'blue': diff_blue}
		
	
	def fade(self, from_time, duration, end_colour):

# 
# 		Calculate time till end
# 			Now + duration = end_time
# 			time till end = end_time - now
# 		calculate colour
# 		current_colour = self.get_lights()
		
		# Calculate time till end
		# Now + duration = end_time
		end_time = from_time + duration

		# Get current light colour
		current_colour = self.get_lights()
		
		
		# Get colours differences
		diffs = self.fade_diffs(current_colour, end_colour)
# 		diff_red = self.fade_diff(end_colour['red'], current_colour['red'])
# 		diff_green = self.fade_diff(end_colour['green'], current_colour['green'])
# 		diff_blue = self.fade_diff(end_colour['blue'], current_colour['blue'])
		
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
			
			colour = self.fade_colours(diffs, percent_remaining)
			self.set_lights(colour)
			if(duration.seconds > 10):
				time.sleep(0.5)

		end_time = time.time()
		print '=' * 10 + ' Elapsed ' + '=' * 10
		print end_time - start_time

		self.set_lights(end_colour)