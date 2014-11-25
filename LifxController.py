import urllib2
import json
from Fade import Fade

# Integration with lifx-http
class LifxController(object):
    HOSTNAME = 'lifx-http.local'
    PORT = 56780
    light_on = False


    def get_lights(self):
        pass

    """
    :type fade Fade
    """
    def set_colour(self, fade):
        fade_dict = fade.get_dict()
        self.__do_request('PUT', '/lights/all/color', fade_dict)

    def lights_on(self):
        pass

    def lights_off(self):
        pass

    def lights_toggle(self):
        pass

    def __do_request(self, request_type, path, body = None):
        url = "http://%s:%d%s" % (self.HOSTNAME, self.PORT, path)
        opener = urllib2.build_opener(urllib2.HTTPHandler)

        if body:
            body = json.JSONEncoder().encode(body)
            request = urllib2.Request(url, data=body)
        else:
            request = urllib2.Request(url)

        request.add_header('Content-Type', 'application/json')
        request.get_method = lambda: request_type
        opener.open(request)