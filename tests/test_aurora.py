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
	
	# @todo cleanup GPIO as setUP runs for each test, which throws errors due to the push-button callback
	def tearDown(self):
# 		self.aurora.shutdown()	
		pass

	def test_get_alarm_for_day_number(self):
		sunday_alarm = self.aurora.get_alarm_for_day_number(0)
		monday_alarm = self.aurora.get_alarm_for_day_number(1)
		tueday_alarm = self.aurora.get_alarm_for_day_number(2)
		wednesday_alarm = self.aurora.get_alarm_for_day_number(3)
		thursday_alarm = self.aurora.get_alarm_for_day_number(4)
		friday_alarm = self.aurora.get_alarm_for_day_number(5)
		saturday_alarm = self.aurora.get_alarm_for_day_number(6)

		print 'sunday   ', sunday_alarm['sunrise']['end_time']
		print 'monday   ', monday_alarm['sunrise']['end_time']
		print 'tueday   ', tueday_alarm['sunrise']['end_time']
		print 'wednesday', wednesday_alarm['sunrise']['end_time']
		print 'thursday ', thursday_alarm['sunrise']['end_time']
		print 'friday   ', friday_alarm['sunrise']['end_time']
		print 'saturday ', saturday_alarm['sunrise']['end_time']

	def test_get_today_alarm(self):
		today_alarm = self.aurora.get_today_alarm()
		print today_alarm
		
# 	def test_next_alarm(self) :
# 		next_alarm = self.aurora.get_next_alarm()
# 		print next_alarm
# 
# 	def test_seconds_till_alarm(self) :
# 		seconds_till_alarm = self.aurora.seconds_till_alarm(datetime.datetime.now() + datetime.timedelta(seconds=10))
#  		self.assertTrue(10 <= seconds_till_alarm <= 10.2)
# 
# 		seconds_till_alarm = self.aurora.seconds_till_alarm(datetime.datetime.now() + datetime.timedelta(days=1))
#  		self.assertTrue(86400 <= seconds_till_alarm <= 86400.2)
# 	
# 	def test_set_alarm(self):	
# 		self.aurora.set_alarm()
	

if __name__ == '__main__':
	unittest.main()