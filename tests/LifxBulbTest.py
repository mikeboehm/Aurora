#!/usr/bin/python
import unittest, os, sys
# from unittest.mock import MagicMock
sys.path.append(os.path.abspath('..'))

import datetime

import LifxBulb
from JsonClient import JsonClient

class TestSettings(unittest.TestCase):
	def setUp(self):
# 		json_client = JsonClient()
		json_client = ''
		self.lifx_bulb = LifxBulb.LifxBulb(json_client)
		
	def test_rgb_to_hsv(self):
#fb0006



		colour = {'red': 0.1, 'green': 0, 'blue': 7}
		print '#' * 20
		print colour
		hsv = self.lifx_bulb.rgb_to_hsv(colour)
		print '^' * 20
		print hsv
		self.assertEquals(0, hsv['hue'])
		self.assertEquals(100, hsv['saturation'])
		self.assertEquals(100, hsv['brightness'])
	
if __name__ == '__main__':
	unittest.main()