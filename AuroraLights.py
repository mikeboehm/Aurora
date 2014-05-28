from Adafruit_PWM_Servo_Driver import PWM
import time
class Lights(object):
	def __init__(self):
		self.pwm = PWM(0x40, debug=True)
		self.freq = 10
		self.pwm.setPWMFreq(self.freq)
		self.red_pin = 1
		self.green_pin = 2
		self.blue_pin = 3

		self.light_state = False
		self.reading_light = {'red' : 255, 'green' : 255, 'blue' : 255}
		self.reading_light['red'] = self.reading_light['red'] * 16
		self.reading_light['green'] = self.reading_light['green'] * 16
		self.reading_light['blue'] = self.reading_light['blue'] * 16
		print 'red: ' + str(self.reading_light['red'])


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

# 		print self.light_state
		if self.light_state:
 			self.toggle_light_off()
			print "turning off"
# 			self.light_state = False
		else :
			self.toggle_light_on()
			print "turning on"
# 			self.light_state = True

	# Turns reading light on
	def toggle_light_on(self):
		print 'toggle_light_on'
# 		self.pwm.setPWM(self.red_pin, 0 , 2000)
# 		time.sleep(0.2)
# 		self.pwm.setPWM(self.red_pin, 0 , 0)
		print self.reading_light['red']
		start_time = time.time()
		for x in range(0,4096, 16):
			red = float(self.reading_light['red']) / 4096.00 * x
			green = float(self.reading_light['green']) / 4096.00 * x
			blue = float(self.reading_light['blue']) / 4096.00 * x
			print red
#
			self.pwm.setPWM(self.red_pin, 0 , int(red))
			self.pwm.setPWM(self.green_pin, 0, int(green))
			self.pwm.setPWM(self.blue_pin, 0, int(blue))

		elapsed_time = time.time() - start_time

		print elapsed_time
# 		print x
# 		print 'red: ' + str(red)
		self.light_state = True
# 		time.sleep(1)

	# Turns reading light off
	def toggle_light_off(self):
		start_time = time.time()
		print 'toggle_light_off'
		print self.reading_light['red']
		print '#' * 20
# 		self.pwm.setPWM(self.blue_pin, 0 , 2000)
# 		time.sleep(0.2)
# 		self.pwm.setPWM(self.blue_pin, 0 , 0)
		for x in range (4096 ,-1, -16):
			print x
			print self.reading_light['red']
			red = self.reading_light['red'] / 4096 * x
			green = self.reading_light['green'] / 4096 * x
			blue = self.reading_light['blue'] / 4096 * x
			colour = {'red' : red, 'green' : green, 'blue' : blue}
			self.set_lights(colour)

# 			self.pwm.setPWM(self.red_pin, 0 , red)
# 			self.pwm.setPWM(self.green_pin, 0, green)
# 			self.pwm.setPWM(self.blue_pin, 0, blue)

# 		print x
		print 'red: ' + str(red)
		self.light_state = False
		elapsed_time = time.time() - start_time

		print elapsed_time


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

		print 'R:' + str(red) + ', G:' + str(green) + ', B:' + str(blue)
		self.pwm.setPWM(self.red_pin, 0 , red)
		self.pwm.setPWM(self.green_pin, 0, green)
		self.pwm.setPWM(self.blue_pin, 0, blue)
	
	def turn_off(self):
		colour = {'red': 0, 'green': 0, 'blue': 0}
		self.set_lights(colour)