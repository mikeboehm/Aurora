#!/usr/bin/python
import unittest, os, sys
from mock import MagicMock
sys.path.append(os.path.abspath('..'))

import datetime

import Settings
from JsonClient import JsonClient

os.system('clear')

class TestSettings(unittest.TestCase):
	mock_settings = {"settings": {"alarms": {"1": {"day": "Monday", "time": "07:00"}, "0": {"day": "Sunday", "time": "08:30"}, "3": {"day": "Wednesday", "time": "07:00"}, "2": {"day": "Tuesday", "time": "07:00"}, "5": {"day": "Friday", "time": "07:00"}, "4": {"day": "Thursday", "time": "07:00"}, "6": {"day": "Saturday", "time": "08:30"}}}}

	def setUp(self):
		json_client = JsonClient()
		json_client = JsonClient()
		json_client.get = MagicMock(return_value=self.mock_settings)

		self.settings = Settings.Settings(json_client)

	def test_magic_mock(self):
		json_client = JsonClient()
		json_client.get = MagicMock(return_value=self.mock_settings)

		mocked = MagicMock(spec=JsonClient)

		print mocked.testicles()

		settings = Settings.Settings(json_client)
		response = settings.get_settings_from_json()
		print '/\\' * 20
# 		print response

# 	def test_get_settings(self):
# 		now = datetime.datetime.now()		
# 		day_number = now.strftime("%w")
# 		print 'day number: ' , day_number
# 		
# 		settings = self.settings.get_settings()
# 		print settings
# 	
# 	def test_get_alarm_for_day(self):
# 		alarm =  self.settings.get_alarm_for_day(0)
# 		print alarm


if __name__ == '__main__':
	unittest.main()