from unittest import TestCase
from mock import MagicMock
import requests
from Lifx import Lifx
from LifxClient import LifxClient

__author__ = 'mike'


class TestLifx(TestCase):
    def setUp(self):
        lifx_client = LifxClient(requests)
        # lifx_client = MagicMock()
        self.lifx = Lifx(lifx_client)

    def tearDown(self):
        self.lifx.fade(self.lifx.NIGHT, 1)

    # def testSetLastSeen(self):
    #     from datetime import datetime
    #     now = datetime.utcnow()
    #     print now.strftime('%Y-%m-%dT%H:%M:%S.%f %Z')
    #
    #     # self.lifx.set_last_seen()
    #
    #     # tester = datetime.strptime('2014-12-06T23:16:25.875+00:00', '%Y-%m-%dT%H:%M:%S%f%Z')
    #     tester = datetime.strptime('2014-12-06T23:16:25.875+00:00', '%Y-%m-%dT%H:%M:%S.%f+00:00')
    #     print tester


    def test_dawn(self):
        response = self.lifx.reading_lights_on()
        self.assertTrue(response)

    def test_sunrise(self):
        self.fail()

    def test_shutoff(self):
        self.fail()

    def test_readinglights_on(self):
        response = self.lifx.reading_lights_on()
        self.assertTrue(response)

    def test_readinglights_off(self):
        response = self.lifx.reading_lights_off()
        self.assertTrue(response)

    def test_readinglights_toggle(self):
        response = self.lifx.readinglights_toggle()
        self.assertTrue(response)
