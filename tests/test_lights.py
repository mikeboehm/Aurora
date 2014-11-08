#!/usr/bin/python
import unittest, os, sys
sys.path.append(os.path.abspath('..'))

import Lights
import datetime
import time
import random
from threading import Thread

# os.system('clear')

class TestAurora(unittest.TestCase):
	def setUp(self):
		self.lights = Lights.Lights()

	def tearDown(self):
		self.cycle({'red': 0, 'green': 0, 'blue': 0})

		
# 	def test_cycle(self) :
# 		print 'colour cycling'
# 		duration = datetime.timedelta(seconds = 2)
# 
# 		end_colour = {'red': 4095, 'green': 0, 'blue': 0}		
# 		fade = {'end_colour': end_colour, 'duration': duration}
# 		self.lights.set_fade(fade)
# 		time.sleep(duration.seconds)
# 
# 		end_colour = {'red': 4095, 'green': 4095, 'blue': 0}		
# 		fade = {'end_colour': end_colour, 'duration': duration}
# 		self.lights.set_fade(fade)
# 		time.sleep(duration.seconds)
# 		
# 		end_colour = {'red': 4095, 'green': 4095, 'blue': 4095}		
# 		fade = {'end_colour': end_colour, 'duration': duration}
# 		self.lights.set_fade(fade)
# 		time.sleep(duration.seconds)
# 
# 		end_colour = {'red': 0, 'green': 4095, 'blue': 4095}		
# 		fade = {'end_colour': end_colour, 'duration': duration}
# 		self.lights.set_fade(fade)
# 		time.sleep(duration.seconds)
		
		
	
# 	def test_turn_on(self) :
# 		print 'test_turn_on'
# 		end_colour = {'red': 4095, 'green': 4095, 'blue': 4095}
# 		duration = datetime.timedelta(seconds = 2)
# 		fade = {'end_colour': end_colour, 'duration': duration}
# 		self.lights.set_fade(fade)
# 		print 'duration.seconds:', duration.seconds
# 		print type(duration.seconds)
# 		time.sleep(duration.seconds)
# 
# 		print 'test_turn_off'
# 		end_colour = {'red': 0, 'green': 0, 'blue': 0}
# 		duration = datetime.timedelta(seconds = 2)
# 		fade = {'end_colour': end_colour, 'duration': duration}
# 		self.lights.set_fade(fade)
# 		time.sleep(duration.seconds)

	def test_cycle(self):
		print 'test_cycle'
		end_colour = {'red': 4095, 'green': 4095, 'blue': 4095}
		self.cycle(end_colour)
		self.cycle({'red': 4095, 'green': 0, 'blue': 0})
		self.cycle({'red': 0, 'green': 4095, 'blue': 0})
		self.cycle({'red': 0, 'green': 0, 'blue': 4095})

	def cycle(self, colour):
		duration = datetime.timedelta(seconds = 2)
		fade = {'end_colour': colour, 'duration': duration}
		self.lights.set_fade(fade)
		time.sleep(duration.seconds)
	
	
if __name__ == '__main__':
	unittest.main()