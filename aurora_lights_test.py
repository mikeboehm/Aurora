#!/usr/bin/python

import AuroraLights
import unittest
import datetime
import time
import os
import random

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
	
	
#	# 	Make sure lights can't be set out of range 	
# 	def test_max_lights(self):
# 		sleep_time = 0.1
# 
# 		colour = {'red': 4096, 'green' : -100, 'blue': -200}
# 		self.lights.set_lights(colour)
# 		tested = self.lights.get_lights()
# 		self.assertEquals(4095, tested['red'])
# 		self.assertEquals(0, tested['green'])
# 		self.assertEquals(0, tested['blue'])
# 		time.sleep(sleep_time)
# 
# 		colour = {'red': 0, 'green' : 4096, 'blue': 0}
# 		self.lights.set_lights(colour)
# 		tested = self.lights.get_lights()
# 		self.assertEquals(4095, tested['green'])
# 		time.sleep(sleep_time)
# 
# 		colour = {'red': 0, 'green' : 0, 'blue': 4096}
# 		self.lights.set_lights(colour)
# 		tested = self.lights.get_lights()
# 		self.assertEquals(4095, tested['blue'])
# 		time.sleep(sleep_time)
# 
# 		self.ligths.turn_off()


# 	def test_turn_off(self) :
# 		colour = {'red': 4095, 'green' : 0, 'blue': 0}
# 		self.lights.set_lights(colour)
# 		post_set  = self.lights.get_lights()
# 		self.assertEquals(post_set['red'], colour['red'])
# 		self.assertEquals(post_set['green'], colour['green'])
# 		self.assertEquals(post_set['blue'], colour['blue'])
# 
# 		
# 		self.lights.turn_off()
# 		colour = self.lights.get_lights()
# 		self.assertEquals(0, colour['red'])
# 		self.assertEquals(0, colour['green'])
# 		self.assertEquals(0, colour['blue'])
	
	
	def test_fade(self):
		from_time = datetime.datetime.now()
		duration = datetime.timedelta(seconds=5)
		end_colour = {'red': 4095, 'green' : 0, 'blue': 0}
		self.lights.fade(from_time, duration, end_colour)
		finished = self.lights.get_lights()
		self.assertEquals(end_colour['red'], finished['red'])
		
		from_time = datetime.datetime.now()
		duration = datetime.timedelta(seconds=5)
		end_colour = {'red': 0, 'green' : 4095, 'blue': 0}
		self.lights.fade(from_time, duration, end_colour)
		finished = self.lights.get_lights()
		self.assertEquals(end_colour['red'], finished['red'])
		self.assertEquals(end_colour['green'], finished['green'])

		from_time = datetime.datetime.now()
		duration = datetime.timedelta(seconds=5)
		end_colour = {'red': 0, 'green' : 0, 'blue': 4095}
		self.lights.fade(from_time, duration, end_colour)
		finished = self.lights.get_lights()
		self.assertEquals(end_colour['red'], finished['red'])
		self.assertEquals(end_colour['green'], finished['green'])
		self.assertEquals(end_colour['blue'], finished['blue'])

		from_time = datetime.datetime.now()
		duration = datetime.timedelta(seconds=5)
		end_colour = {'red': 0, 'green' : 0, 'blue': 0}
		self.lights.fade(from_time, duration, end_colour)
		finished = self.lights.get_lights()
		self.assertEquals(end_colour['red'], finished['red'])
		self.assertEquals(end_colour['green'], finished['green'])
		self.assertEquals(end_colour['blue'], finished['blue'])


 		
# 	def test_get_lights(self):
# 		for x in xrange(3):
# 			colour = {'red': random.randint(0,4095), 'green' : random.randint(0,4095), 'blue': random.randint(0,4095)}
# 			self.lights.set_lights(colour)
# 			got_lights = self.lights.get_lights()
# 			self.assertEqual(colour['red'], got_lights['red'])
# 			self.assertEqual(colour['green'], got_lights['green'])
# 			self.assertEqual(colour['blue'], got_lights['blue'])
# 		
# 		self.lights.turn_off()


if __name__ == '__main__':
	unittest.main()