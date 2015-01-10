import json
import datetime
from Globe import Globe


class LifxClient(object):
    # BASE_URL = 'http://lifx-http.local:56780'
    # BASE_URL = 'http://localhost:56780'
    BASE_URL = 'http://127.0.0.1:56780'
    # BASE_URL = 'http://aurora.local:56780'
    ENDPOINT_GET_LIGHTS = '/lights.json'
    ENDPOINT_TOGGLE = '/lights/all/toggle'
    ENDPOINT_LIGHTS_ON = '/lights/all/on'
    ENDPOINT_LIGHTS_OFF = '/lights/all/off'
    ENDPOINT_SET_LIGHTS = '/lights/all/color'

    def __init__(self, requests):
        self.requests = requests

    def do_put(self, url, payload=None):
        try:
            response = self.requests.put(url, payload)
            return self.convert_response(response.text)
        except Exception as e:
            print '*' * 20
            print e.message
            print '*' * 20

        return False

    def do_get(self, url):
        try:
            response = self.requests.get(url)
            # print response.text
            return self.convert_response(response.text)
        except Exception as e:
            print '*' * 20
            print e.message
            print '*' * 20
            return False

    def toggle(self):
        url = self.url_builder(self.ENDPOINT_TOGGLE)
        return self.do_put(url)

    def turn_on(self):
        url = self.url_builder(self.ENDPOINT_LIGHTS_ON)
        return self.do_put(url)

    def turn_off(self):
        url = self.url_builder(self.ENDPOINT_LIGHTS_OFF)
        return self.do_put(url)

    def fade(self, color, duration):
        url = self.url_builder(self.ENDPOINT_SET_LIGHTS)

        color['duration'] = self.get_duration_in_seconds(duration)

        return self.do_put(url, color)

    def get_lights(self):
        url = self.url_builder(self.ENDPOINT_GET_LIGHTS)
        return self.do_get(url)

    @staticmethod
    def convert_response(response):
        lights_dict_array = json.loads(response)
        lights = []
        for light_dict in lights_dict_array:
            light = Globe(light_dict)
            lights.append(light)

        return lights

    def url_builder(self, endpoint):
        return self.BASE_URL + endpoint

    @staticmethod
    def get_duration_in_seconds(duration):
        if isinstance(duration, datetime.timedelta):
            duration_in_seconds = duration.total_seconds()
        else:
            duration_in_seconds = duration

        return duration_in_seconds
        