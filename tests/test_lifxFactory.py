from unittest import TestCase
import json

from lifx_factory import LifxFactory

__author__ = 'mike'


class TestLifxFactory(TestCase):
    lifx_all_on = '[{"id":"d073d501f660","label":"Dresser","site_id":"4c4946585632","tags":[],"on":true,"color":{"hue":63.705195696955826,"saturation":0.0,"brightness":0.01998931868467231,"kelvin":2500},"last_seen":"2015-02-17T20:02:02.670+00:00","seconds_since_seen":533.584032508},{"id":"d073d501bd50","label":"Lounge","site_id":"4c4946585632","tags":[],"on":true,"color":{"hue":28.99336232547494,"saturation":0.9827420462348363,"brightness":1.0,"kelvin":3500},"last_seen":"2015-02-17T20:01:55.775+00:00","seconds_since_seen":540.482364822}]'


    def setUp(self):
        self.lifx_response = json.loads(self.lifx_raw)
        self.lifx_factory = LifxFactory

    def test_create_globe(self):
        print self.lifx_response
        self.fail()

    def test_create_bulb_collection(self):
        self.fail()