#!/usr/bin/python
import unittest, os, sys
sys.path.append(os.path.abspath('..'))

import AuroraSunrise
import datetime
import time

class TestAuroraSunrise(unittest.TestCase):

	def setUp(self):
		self.sunrise = AuroraLights.Sunrise()

# 	def test_toggle_light(self):
# 		self.lights.toggle_light_off()

	
if __name__ == '__main__':
	unittest.main()