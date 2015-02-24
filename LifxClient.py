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

    logger = None

    def __init__(self, request_handler, logger):
        """
        :type request_handler: requests
        """
        self.request_handler = request_handler

        self.logger = logger
        self._log('init()')

    def do_put(self, url, payload=None):
        self._log('do_put()')
        try:
            response = self.request_handler.put(url, payload)
            return self.convert_response(response)
        except Exception as e:
            print '*' * 20
            print e.message
            print '*' * 20

        return False

    def do_get(self, url):
        self._log('do_get()')
        try:
            response = self.request_handler.get(url)
            # print response.text
            return self.convert_response(response)
        except Exception as e:
            print '*' * 20
            print e.message
            print '*' * 20
            return False

    def toggle(self):
        self._log('toggle()')
        url = self.url_builder(self.ENDPOINT_TOGGLE)
        return self.do_put(url)

    def turn_on(self):
        self._log('turn_on()')
        url = self.url_builder(self.ENDPOINT_LIGHTS_ON)
        return self.do_put(url)

    def turn_off(self):
        self._log('turn_off()')
        url = self.url_builder(self.ENDPOINT_LIGHTS_OFF)
        return self.do_put(url)

    def fade(self, color, duration):
        self._log('fade()')
        url = self.url_builder(self.ENDPOINT_SET_LIGHTS)

        color['duration'] = self.get_duration_in_seconds(duration)

        return self.do_put(url, color)

    def get_lights(self):
        self._log('get_lights()')
        url = self.url_builder(self.ENDPOINT_GET_LIGHTS)
        return self.do_get(url)

    def convert_response(self, response):
        response_text = response.text
        self._log('convert_response()')
        self._log(response.status_code)
        self._log(response_text)

        lights_dict_array = json.loads(response_text)
        lights = []
        for light_dict in lights_dict_array:
            light = Globe(light_dict)
            lights.append(light)

        return lights

    def url_builder(self, endpoint):
        return self.BASE_URL + endpoint

    # @staticmethod
    def get_duration_in_seconds(self, duration):
        self._log('get_duration_in_seconds()')
        if isinstance(duration, datetime.timedelta):
            duration_in_seconds = duration.total_seconds()
        else:
            duration_in_seconds = duration

        return duration_in_seconds

    def _log(self, method_name, message=None):
        log_line = str(method_name)

        if message:
            log_line += ': ' + str(message)

        self.logger.write(log_line, 'LifxClient')