#!/usr/bin/python
import unittest, os, sys
sys.path.append(os.path.abspath('..'))

import Aurora
import datetime
import time
import random
from threading import Thread

# os.system('clear')

class TestAurora(unittest.TestCase):
	def setUp(self):
		self.aurora = Aurora.Aurora()
		
	def test_next_alarm(self) :
		next_alarm = self.aurora.get_next_alarm()
		print next_alarm

	def test_seconds_till_alarm(self) :
		seconds_till_alarm = self.aurora.seconds_till_alarm(datetime.datetime.now() + datetime.timedelta(seconds=10))
 		self.assertTrue(10 <= seconds_till_alarm <= 10.2)

		seconds_till_alarm = self.aurora.seconds_till_alarm(datetime.datetime.now() + datetime.timedelta(days=1))
 		self.assertTrue(86400 <= seconds_till_alarm <= 86400.2)
	
	def test_set_alarm(self):	
		self.aurora.set_alarm()
	

if __name__ == '__main__':
	unittest.main()