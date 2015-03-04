from unittest import TestCase
import json
from dateutil import parser

from hsbk_color import HSBKColor
from lifx_globe import LifxGlobe

__author__ = 'mike'


class TestLifxGlobe(TestCase):
    def test_construction(self):
        raw_json = '[{"id":"d073d500ec68","label":"Bedroom","site_id":"4c4946585632","tags":["1.5"],"on":false,"color":{"hue":0.0,"saturation":0.0,"brightness":1.0,"kelvin":9000},"last_seen":"2015-02-24T08:41:38.818+00:00","seconds_since_seen":6.174382}]'
        lights_dict_array = json.loads(raw_json)

        lights = self.light_factory(lights_dict_array)

        print lights

        for light in lights:
            print light.tags


    def light_factory(self, lights_dict_array):
        lights = []
        for light_dict in lights_dict_array:
            id = light_dict['id']
            label = light_dict['label']
            site_id = light_dict['site_id']
            tags = light_dict['tags']
            on = light_dict['on']
            color = light_dict['color']

            last_seen = parser.parse(light_dict['last_seen'])
            seconds_since_seen = light_dict['seconds_since_seen']

            color = HSBKColor(color['hue'], color['saturation'], color['brightness'], color['kelvin'])

            light = LifxGlobe(id, label, site_id, tags, on, color, last_seen, seconds_since_seen)
            lights.append(light)

        return lights
