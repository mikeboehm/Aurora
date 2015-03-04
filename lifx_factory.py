from dateutil import parser

from lifx_globe import LifxGlobe
from hsbk_color import HSBKColor


class LifxFactory(object):

    def create_globe(self, light_dict):
        lifx_id = light_dict['id']
        label = light_dict['label']
        site_id = light_dict['site_id']
        tags = light_dict['tags']
        on = light_dict['on']
        color = light_dict['color']

        last_seen = parser.parse(light_dict['last_seen'])
        seconds_since_seen = light_dict['seconds_since_seen']

        color = HSBKColor(color['hue'], color['saturation'], color['brightness'], color['kelvin'])

        light = LifxGlobe(lifx_id, label, site_id, tags, on, color, last_seen, seconds_since_seen)

        return light

    def create_bulb_collection(self, light_dict_array):
        lights = []
        for light in light_dict_array:
            lifx_globe = self.create_globe(light)
            lights.append(lifx_globe)

        return lights