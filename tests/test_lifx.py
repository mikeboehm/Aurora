from unittest import TestCase
import requests
import time
from Lifx import Lifx
from LifxClient import LifxClient
from fake_logger import FakeLogger

__author__ = 'mike'


class TestLifx(TestCase):
    def setUp(self):
        logger = FakeLogger()
        lifx_client = LifxClient(requests, logger)
        self.lifx = Lifx(lifx_client, logger)

    def test_dawn(self):
        self.fail()

    def test_sunrise(self):
        self.fail()

    def test_shutoff(self):
        self.fail()

    def test_threaded_toggle(self):
        self.lifx.threaded_toggle()
        print 'lights_are_on: ', self.lifx.lights_are_on
        print 'Now sleeping'
        time.sleep(5)
        print 'Done sleeping'

        self.lifx.threaded_toggle()
        print 'lights_are_on:', self.lifx.lights_are_on

    def test_reading_lights_on(self):
        self.fail()

    def test_reading_lights_off(self):
        self.fail()

    def test_reading_lights_toggle(self):
        self.fail()

    def test__log(self):
        self.fail()