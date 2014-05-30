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

# 	def test_toggle_light(self):
# 		self.lights.toggle_light_off()

# 	def test_toggle_light(self):
# 		self.lights.toggle_light(1)
# 		time.sleep(1)
# 		self.lights.toggle_light(1)
	
	def test_fade(self):
		from_time = datetime.datetime.now()
		duration = datetime.timedelta(seconds=5)
		end_colour = {'red': 4095, 'green' : 0, 'blue': 0}
		self.lights.fade(from_time, duration, end_colour)
		
	def test_get_lghts(self):
		pass
	
# 		self.lights.get_lghts()
	
if __name__ == '__main__':
	unittest.main()