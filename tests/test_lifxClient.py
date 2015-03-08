from unittest import TestCase
from mock import MagicMock
import requests
import time
import datetime
from LifxClient import LifxClient
from Globe import Globe
from fake_logger import FakeLogger

__author__ = 'mike'

class TestLifxClient(TestCase):
    def setUp(self):
        # request = MagicMock()
        request = requests
        logger = FakeLogger()
        self.lifx = LifxClient(request, logger)

    def test_toggle(self):
        current_state = self.lifx.get_lights()

        current_on_state = current_state[0].get_light_state()
        print '#' * 20
        print current_on_state
        print '#' * 20

        response = self.lifx.toggle()
        self.assertNotEqual(current_on_state, response[0].get_light_state())

    def test_turn_on(self):
        response = self.lifx.turn_on()
        self.assertTrue(response[0].get_light_state())


    def test_turn_off(self):
        response = self.lifx.turn_off()
        self.assertFalse(response[0].get_light_state())

    def test_fade(self):
        # print '$' * 30
        # print 'Initial get_Lights'
        print 'Initial:', self.lifx.get_lights()[0].get_color()


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
        duration = datetime.timedelta(seconds=10)
        delay = datetime.timedelta(seconds=1) + duration
        self.lifx.turn_on()
        self.lifx.fade(red, duration)
        time.sleep(delay.total_seconds())
        lights = self.lifx.get_lights()

        print 'Red    :', lights[0].get_color()

        # self.assertAlmostEquals(round(red['saturation'],4), round(lights[0].get_color()['saturation'],4))

        self.lifx.fade(black, duration)
        time.sleep(delay.total_seconds())
        lights = self.lifx.get_lights()
        print 'Black  :', lights[0].get_color()

        # self.assertAlmostEquals(round(black['saturation'],4), round(lights[0].get_color()['saturation'],4))


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
        self.lifx.turn_on()
        self.lifx.fade(red, 20)
        time.sleep(duration.total_seconds())



        # Sunrise
        print '# Sunrise'
        self.lifx.fade(white, duration)
        time.sleep(duration.total_seconds())

        # Shut-off
        print '# Shut-off'
        shutoff_time = datetime.timedelta(seconds=2)
        time.sleep(duration.total_seconds())
        self.lifx.fade(dim, shutoff_time)
        time.sleep(duration.total_seconds())
        self.lifx.fade(black, shutoff_time)
        self.lifx.turn_off()
        # self.fail()

    def test_get_lights(self):
        lights = self.lifx.get_lights()

        count = 0
        for light in lights:
            self.assertIsInstance(light, Globe)
            count += 1

        self.assertGreaterEqual(1, count)

    def test_url_buidler(self):
        endpoint = 'lights'
        url = self.lifx.url_builder(endpoint)
        url = str(url)
        self.assertTrue(url.endswith(endpoint))

    def test_get_duration_in_seconds(self):
        seconds_as_integer = 10
        result = self.lifx.get_duration_in_seconds(seconds_as_integer)
        self.assertEquals(seconds_as_integer, result)

        seconds_as_string = '15'
        result = self.lifx.get_duration_in_seconds(seconds_as_string)
        self.assertEquals(seconds_as_string, result)

        td_seconds = 20
        seconds_as_timedelta = datetime.timedelta(seconds=td_seconds)
        result = self.lifx.get_duration_in_seconds(seconds_as_timedelta)
        self.assertEquals(20, result)

    def test_convert_response(self):
        mock_response = '[{"id":"d073d501f660","label":"","site_id":"4c4946585632","tags":["Bedroom"],"on":false,"color":{"hue":0.0,"saturation":0.0,"brightness":0.010009918364232854,"kelvin":2500},"last_seen":"2014-12-04T22:48:00.512+00:00","seconds_since_seen":2.87203}]'
        response = self.lifx.convert_response(mock_response)

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], Globe)
        self.assertFalse(response[0].get_light_state())
        self.assertIsNotNone(response[0].get_color())

    def test_get(self):
        url = 'http://httpbin.org/status/200'
        """
        :type response: requests.Response
        """
        response = self.lifx.request_handler.get(url)

        self.assertEquals(200, response.status_code)
