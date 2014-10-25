#!/usr/bin/python
import unittest, os, sys
# from unittest.mock import MagicMock
sys.path.append(os.path.abspath('..'))

import Settings
from JsonClient import JsonClient

class TestSettings(unittest.TestCase):
	def setUp(self):
		json_client = JsonClient()
		self.settings = Settings.Settings(json_client)
		
	def test_get_settings(self):
		settings = self.settings.get_settings()
		print settings
	
	def test_get_alarm_for_day(self):
		alarm =  self.settings.get_alarm_for_day(0)
		print alarm
	
	
if __name__ == '__main__':
	unittest.main()