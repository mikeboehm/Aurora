from unittest import TestCase
from mock import MagicMock
import requests
import time
from Lifx import Lifx
from Globe import Globe

__author__ = 'mike'

class TestLifx(TestCase):
    def setUp(self):
        # request = MagicMock()
        request = requests
        self.Lifx = Lifx(request)

    def test_toggle(self):
        pass
        # self.fail()

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
        duration = 2
        self.Lifx.fade(red, duration)
        time.sleep(duration)

        lights = self.Lifx.get_lights()
        print lights
        self.assertEquals(red, lights[0].get_color())

        self.Lifx.fade(black, duration)
        time.sleep(duration)


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
            'saturation': 0,
            'brightness': 0,
            'kelvin': 2500
        }

        duration = 5

        self.Lifx.turn_on()
        self.Lifx.fade(red, duration)
        time.sleep(duration)

        self.Lifx.fade(white, duration)
        time.sleep(duration)

        self.Lifx.fade(black, duration)
        time.sleep(duration)
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
        url = self.Lifx.url_buidler(endpoint)
        url = str(url)
        self.assertTrue(url.endswith(endpoint))