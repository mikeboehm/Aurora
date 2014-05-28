#!/usr/bin/python

import AuroraLights
import unittest
import datetime
import time

class TestAuroraLights(unittest.TestCase):

	def setUp(self):
		self.lights = AuroraLights.Lights()

# 	def test_toggle_light(self):
# 		self.lights.toggle_light_off()

	def test_toggle_light(self):
		self.lights.toggle_light(1)
		time.sleep(1)
		self.lights.toggle_light(1)
	
if __name__ == '__main__':
	unittest.main()