#!/usr/bin/python
import unittest, os, sys
sys.path.append(os.path.abspath('..'))

import AuroraLights
import datetime
import time
import random
from threading import Thread

os.system('clear')

class TestAuroraLights(unittest.TestCase):

	def setUp(self):
		self.lights = AuroraLights.Lights()

	def tearDown(self):
		colour  = {'red' : 0, 'green' : 0, 'blue' : 0}
		self.lights.set_lights(colour)

	def fade(self):
		now = datetime.datetime.now()
		colour  = {'red' : 2095, 'green' : 2095, 'blue' : 0}
		print now
		print now
		print now
		print now
		print now
		print now
# 		self.lights.fade(now)
	

	def test_toggle_light(self):
		now = datetime.datetime.now()
		colour  = {'red' : random.randint(0, 4095), 'green' : random.randint(0, 4095), 'blue' : random.randint(0, 4095)}
		duration = datetime.timedelta(seconds=10)

		t = Thread(target=self.lights.fade, args=(now, duration, colour))
		print 'already finished' 
		t.start()

if __name__ == '__main__':
	unittest.main()