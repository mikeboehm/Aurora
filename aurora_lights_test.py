#!/usr/bin/python

import AuroraLights
import unittest
import datetime
import time
import os

os.system('clear')

class TestAuroraLights(unittest.TestCase):

	def setUp(self):
		self.lights = AuroraLights.Lights()

	def tearDown(self):
		colour  = {'red' : 0, 'green' : 0, 'blue' : 0}
		self.lights.set_lights(colour)


# 	def test_toggle_light(self):
# 		self.lights.toggle_light_off()

# 	def test_toggle_light(self):
# 		self.lights.toggle_light(1)
# 		time.sleep(1)
# 		self.lights.toggle_light(1)
	
	
	# 	Make sure lights can't be set out of range 	
	def test_max_lights(self):
		colour = {'red': 4096, 'green' : -100, 'blue': -200}
		self.lights.set_lights(colour)
		tested = self.lights.get_lights()
		self.assertEquals(4095, tested['red'])
		self.assertEquals(0, tested['green'])
		self.assertEquals(0, tested['blue'])
		time.sleep(1)
		colour = {'red': 0, 'green' : 4096, 'blue': 0}
		self.lights.set_lights(colour)
		time.sleep(1)
		colour = {'red': 0, 'green' : 0, 'blue': 4096}
		self.lights.set_lights(colour)
		time.sleep(1)
		colour = {'red': 0, 'green' : 0, 'blue': 0}
		self.lights.set_lights(colour)


	
# 	def test_fade(self):
# 		from_time = datetime.datetime.now()
# 		duration = datetime.timedelta(seconds=5)
# 		end_colour = {'red': 4095, 'green' : 0, 'blue': 0}
# 		self.lights.fade(from_time, duration, end_colour)
# 		
# 	def test_get_lghts(self):
# 		pass
	
# 		self.lights.get_lghts()


if __name__ == '__main__':
	unittest.main()