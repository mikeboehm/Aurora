#!/usr/bin/python
import unittest, os, sys
sys.path.append(os.path.abspath('..'))

import AuroraLights
import datetime
import time
import random
from threading import Thread

# os.system('clear')

class TestAuroraLights(unittest.TestCase):

	def setUp(self):
		print 'hi!'
		self.lights = AuroraLights.Lights()

	def tearDown(self):
		colour  = {'red' : 0, 'green' : 0, 'blue' : 0}
		self.lights.set_lights(colour)

	def test_fade_thread_test(self) :
		print 'fade_thread_test'		
# 		random.randint(0, 4095)
		
		duration = datetime.timedelta(seconds=10)
		sleep_duration = datetime.timedelta(seconds=5)

		time.sleep(0.5)
		colour  = {'red' : 4095, 'green' : 0, 'blue' : 0}
		print 'set_fade'
		self.lights.set_fade(duration, colour)
		time.sleep(sleep_duration.seconds)
		
		reading_light_duration = datetime.timedelta(seconds=1)
		colour  = {'red' : 4095, 'green' : 4095, 'blue' : 4095}
		print 'set_fade'
		self.lights.set_fade(reading_light_duration, colour)		
		time.sleep(1)

		reading_light_duration = datetime.timedelta(seconds=1)
		colour  = {'red' : 0, 'green' : 0, 'blue' : 0}
		print 'set_fade'
		self.lights.set_fade(reading_light_duration, colour)		
		time.sleep(1)

		
# 		colour  = {'red' : 0, 'green' : 0, 'blue' : 4095}
# 		print 'set_fade'
# 		self.lights.set_fade(duration, colour)
# 		time.sleep(sleep_duration.seconds)
		
		colour  = {'red' : 4095, 'green' : 4095, 'blue' : 0}
		print 'set_fade'
		self.lights.set_fade(duration, colour)
		time.sleep(sleep_duration.seconds)
		
		colour  = {'red' : 0, 'green' : 0, 'blue' : 0}
		print 'set_fade'
		self.lights.set_fade(duration, colour)
		time.sleep(sleep_duration.seconds)
		self.lights.kill_fade()
	
	def fade(self):
		print 'fade'
		now = datetime.datetime.now()
		colour  = {'red' : 2095, 'green' : 2095, 'blue' : 0}
# 		self.lights.fade(now)
	

# 	def test_toggle_light(self):
# 		now = datetime.datetime.now()
# 		colour  = {'red' : random.randint(0, 4095), 'green' : random.randint(0, 4095), 'blue' : random.randint(0, 4095)}
# 		duration = datetime.timedelta(seconds=10)
# 
# 		t = Thread(target=self.lights.fade, args=(now, duration, colour))
# 		print 'already finished' 
# 		t.start()

if __name__ == '__main__':
	unittest.main()