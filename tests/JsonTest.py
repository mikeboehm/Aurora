#!/usr/bin/python
import unittest, os, sys
sys.path.append(os.path.abspath('..'))

import JsonClient

class TestSettings(unittest.TestCase):
	def setUp(self):
		self.json_client = JsonClient.JsonClient()		
	
	def test_get_json(self):
		returned_json = self.json_client.get('http://ip.jsontest.com/')
		
		contains_ip = False
		if(returned_json['ip']):
			contains_ip = True
		self.assertTrue(contains_ip)
		
	
if __name__ == '__main__':
	unittest.main()