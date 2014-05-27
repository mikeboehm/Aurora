#!/usr/bin/python

import AuroraSettings
import unittest
import datetime
import random

class TestAuroraSettings(unittest.TestCase):

	def setUp(self):
		self.seq = range(10)
		self.settings = AuroraSettings.settings()

	def test_get_dawn_duration(self):
		duration = self.settings.get_dawn_duration()
		test_duration = datetime.timedelta(hours=0, minutes=30)
		self.assertIsInstance(duration, datetime.timedelta)

	def test_get_shutoff_delay(self):
		duration = self.settings.get_shutoff_delay()
		test_duration = datetime.timedelta(hours=1, minutes=0)
		self.assertIsInstance(duration, datetime.timedelta)
	
	def test_get_alarms(self):
		alarms = self.settings.get_alarms()
		monday = alarms['Monday']
		Tuesday = alarms['Tuesday']
		Wednesday = alarms['Wednesday']
		Thursday = alarms['Thursday']
		Friday = alarms['Friday']
		Saturday = alarms['Saturday']
		Sunday = alarms['Sunday']
		self.assertIsInstance(monday, datetime.datetime)
		self.assertIsInstance(Tuesday, datetime.datetime)
		self.assertIsInstance(Wednesday, datetime.datetime)
		self.assertIsInstance(Thursday, datetime.datetime)
		self.assertIsInstance(Friday, datetime.datetime)
		self.assertIsInstance(Saturday, datetime.datetime)
		self.assertIsInstance(Sunday, datetime.datetime)
	
	def test_get_alarm(self):
		alarm = self.settings.get_alarm('Monday')
		print alarm
		self.assertIsInstance(alarm, AuroraAlarm.Alarm)
	
if __name__ == '__main__':
	unittest.main()