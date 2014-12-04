from unittest import TestCase
from mock import MagicMock
import requests
import time
import datetime
from LifxClient import LifxClient
from Globe import Globe

__author__ = 'mike'

class TestLifxClient(TestCase):
    def setUp(self):
        # request = MagicMock()
        request = requests
        self.Lifx = LifxClient(request)

    def test_toggle(self):
        response = self.Lifx.toggle()

        self.assertIsNot(False, response)

    def test_turn_on(self):
        pass
        # self.fail()

    def test_turn_off(self):
        pass
        # self.fail()

    def test_fade(self):
        red = {
            'hue': 0,
            'saturation': 0.32018,
            'brightness': 0.14474,
            'kelvin': 2500
        }

        black = {
            'hue': 0,
            'saturation': 0,
            'brightness': 0,
            'kelvin': 2500
        }
        duration = datetime.timedelta(seconds=2)
        delay = datetime.timedelta(seconds=1)
        delay += duration
        self.Lifx.turn_on()
        self.Lifx.fade(red, duration)
        time.sleep(delay.total_seconds())

        lights = self.Lifx.get_lights()
        print '=' * 20
        print lights
        print '=' * 20
        self.assertEquals(red, lights[0].get_color())

        self.Lifx.fade(black, duration)
        time.sleep(delay.total_seconds())


    def test_sunrise(self):
        red = {
            'hue': 0,
            'saturation': 1,
            'brightness': 1,
            'kelvin': 2500
        }

        white = {
            'hue': 0,
            'saturation': 0,
            'brightness': 1,
            'kelvin': 2500
        }

        black = {
            'hue': 0,
            'saturation': 1,
            'brightness': 0,
            'kelvin': 2500
        }

        dim = {
            'hue': 0,
            'saturation': 0,
            'brightness': 0,
            'kelvin': 2500
        }

        duration = datetime.timedelta(seconds=10)

        # Dawn
        print '# Dawn'
        self.Lifx.turn_on()
        self.Lifx.fade(red, 20)
        time.sleep(duration.total_seconds())



        # Sunrise
        print '# Sunrise'
        self.Lifx.fade(white, duration)
        time.sleep(duration.total_seconds())

        # Shut-off
        print '# Shut-off'
        shutoff_time = datetime.timedelta(seconds=2)
        time.sleep(duration.total_seconds())
        self.Lifx.fade(dim, shutoff_time)
        time.sleep(duration.total_seconds())
        self.Lifx.fade(black, shutoff_time)
        self.Lifx.turn_off()
        # self.fail()

    def test_get_lights(self):
        lights = self.Lifx.get_lights()

        count = 0
        for light in lights:
            self.assertIsInstance(light, Globe)
            count += 1

        self.assertGreaterEqual(1, count)

    def test_url_buidler(self):
        endpoint = 'lights'
        url = self.Lifx.url_builder(endpoint)
        url = str(url)
        self.assertTrue(url.endswith(endpoint))

    def test_get_duration_in_seconds(self):
        seconds_as_integer = 10
        result = self.Lifx.get_duration_in_seconds(seconds_as_integer)
        self.assertEquals(seconds_as_integer, result)

        seconds_as_string = '15'
        result = self.Lifx.get_duration_in_seconds(seconds_as_string)
        self.assertEquals(seconds_as_string, result)

        td_seconds = 20
        seconds_as_timedelta = datetime.timedelta(seconds=td_seconds)
        result = self.Lifx.get_duration_in_seconds(seconds_as_timedelta)
        self.assertEquals(20, result)

    def test_convert_response(self):
        mock_response = '[{"id":"d073d501f660","label":"","site_id":"4c4946585632","tags":["Bedroom"],"on":false,"color":{"hue":0.0,"saturation":0.0,"brightness":0.010009918364232854,"kelvin":2500},"last_seen":"2014-12-04T22:48:00.512+00:00","seconds_since_seen":2.87203}]'
        response = self.Lifx.convert_response(mock_response)

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertTrue(('on' in response[0]))
        self.assertTrue(('color' in response[0]))
