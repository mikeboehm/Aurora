import json
import datetime
from Globe import Globe
class LifxClient(object):
    # BASE_URL = 'http://lifx-http.local:56780'
    BASE_URL = 'http://localhost:56780'
    # BASE_URL = 'http://aurora.local:56780'
    ENDPOINT_GET_LIGHTS = '/lights.json'
    ENDPOINT_TOGGLE = '/lights/all/toggle'
    ENDPOINT_LIGHTS_ON = '/lights/all/on'
    ENDPOINT_LIGHTS_OFF = '/lights/all/off'
    ENDPOINT_SET_LIGHTS = '/lights/all/color'

    DAWN = {
        'hue': 0,
        'saturation': 1,
        'brightness': 1,
        'kelvin': 2500
    }

    DAY = {
        'hue': 0,
        'saturation': 0,
        'brightness': 1,
        'kelvin': 2500
    }

    NIGHT = {
        'hue': 0,
        'saturation': 0,
        'brightness': 0,
        'kelvin': 2500
    }

    READING_LIGHT = {
        'hue': 0,
        'saturation': 1,
        'brightness': 0.25,
        'kelvin': 2500
    }

    def __init__(self, requests):
        self.requests = requests
        pass

    def toggle(self):
        url = self.url_builder(self.ENDPOINT_LIGHTS_ON)
        return self.requests.put(url)


    def turn_on(self):
        url = self.url_builder(self.ENDPOINT_LIGHTS_ON)
        self.requests.put(url)

    def turn_off(self):
        url = self.url_builder(self.ENDPOINT_LIGHTS_OFF)
        self.requests.put(url)

    def fade(self, color, duration):
        url = self.url_builder(self.ENDPOINT_SET_LIGHTS)

        color['duration'] = self.get_duration_in_seconds(duration)

        response = self.requests.put(url, color)

    def get_lights(self):
        url = self.url_builder(self.ENDPOINT_GET_LIGHTS)
        response = self.requests.get(url)
        lights_dict_array = json.loads(response.text)
        lights = []
        for light_dict in lights_dict_array:
            light = Globe(light_dict)
            lights.append(light)

        return lights

    def url_builder(self, endpoint):
        return self.BASE_URL + endpoint

    def get_duration_in_seconds(self, duration):
        if isinstance(duration, datetime.timedelta):
            duration_in_seconds = duration.total_seconds()
            print type(duration)
        else:
            duration_in_seconds = duration

        return duration_in_seconds