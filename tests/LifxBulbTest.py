#!/usr/bin/python
import unittest, os, sys
import urllib, json
import time
# from unittest.mock import MagicMock
sys.path.append(os.path.abspath('..'))
os.system('clear')

import datetime

import LifxBulb
from JsonClient import JsonClient

class TestSettings(unittest.TestCase):
    url = 'http://localhost:56780/lights.json'

    def setUp(self):
        json_client = JsonClient()
        self.lifx_bulb = LifxBulb.LifxBulb(json_client)

    def test_get_lights_returns_a_list(self):
        lights = self.lifx_bulb.get_lights()
        self.assertIsInstance(lights, list)

    def test_sunrise(self):
        delay = 0.5
        # Black
        duration = 0.5
        black = {
            "hue": 0,
            "duration": duration,
            "saturation" : 1,
            "brightness" : 0,
            "kelvin": 2500
        }
        self.lifx_bulb.set_colour(black)
        time.sleep(duration + delay)

        # Test black
        lights = self.lifx_bulb.get_lights()
        print lights
        self.assertEquals(black['hue'], lights[0]['color']['hue'])
        self.assertEquals(black['saturation'], lights[0]['color']['saturation'])
        self.assertEquals(black['brightness'], lights[0]['color']['brightness'])
        self.assertEquals(black['kelvin'], lights[0]['color']['kelvin'])

        # Red
        duration = 0.5
        red = {
            "hue": 0,
            "duration": duration,
            "saturation" : 1,
            "brightness" : 1,
            "kelvin": 2500
        }
        print 'set red'
        self.lifx_bulb.set_colour(red)
        time.sleep(duration + delay)

        # Test red
        lights = self.lifx_bulb.get_lights()
        print lights
        self.assertEquals(red['hue'], lights[0]['color']['hue'])
        self.assertEquals(red['saturation'], lights[0]['color']['saturation'])
        self.assertEquals(red['brightness'], lights[0]['color']['brightness'])
        self.assertEquals(red['kelvin'], lights[0]['color']['kelvin'])

        duration = 0.5
        white = {
            "hue": 0,
            "duration": duration,
            "saturation" : 0,
            "brightness" : 1,
            "kelvin": 2500
        }
        print 'set white'
        self.lifx_bulb.set_colour(white)
        time.sleep(duration + delay)
        lights = self.lifx_bulb.get_lights()
        self.assertEquals(white['hue'], lights[0]['color']['hue'])
        self.assertEquals(white['saturation'], lights[0]['color']['saturation'])
        self.assertEquals(white['brightness'], lights[0]['color']['brightness'])
        self.assertEquals(white['kelvin'], lights[0]['color']['kelvin'])

        print 'set black'
        duration = 0.5
        black = {
            "hue": 0,
            "duration": duration,
            "saturation" : 1,
            "brightness" : 0,
            "kelvin": 2500
        }
        time.sleep(duration)
        self.lifx_bulb.set_colour(black)

# 	def test_bulb_is_off_and_turns_on(self):
# 		lights = self.lifx_bulb.get_lights()
# 		self.assertEquals(False, lights[0]['on'])
# 
# 		self.lifx_bulb.set_lights_on()
# 
# 		lights = self.lifx_bulb.get_lights()		
# 		self.assertEquals(True, lights[0]['on'])



if __name__ == '__main__':
    unittest.main()