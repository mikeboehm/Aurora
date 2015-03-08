from unittest import TestCase
from mock import MagicMock
from Aurora import Aurora

__author__ = 'mike'


class TestAurora(TestCase):
    def setUp(self):
        lights = MagicMock()
        settings = MagicMock()
        gpio_controller = MagicMock()
        logger = MagicMock()

        self.aurora = Aurora(lights, settings, gpio_controller, logger)

    def test_toggle_light_callback(self):
        self.fail()

    def test_rabbit_listener(self):
        self.fail()

    def test_rabbit_callback(self):
        self.fail()

    def test_get_settings(self):
        self.fail()

    def test_set_alarm(self):
        self.fail()

    def test_trigger_dawn(self):
        self.fail()

    def test_trigger_sunrise(self):
        self.fail()

    def test_trigger_autoshutoff(self):
        self.fail()

    def test_seconds_till_alarm(self):
        self.fail()

    def test_get_alarm_for_day_number(self):
        self.fail()

    def test_get_today_alarm(self):
        self.fail()

    def test_get_next_alarm(self):
       self.fail()


    def test_shutdown(self):
        self.fail()