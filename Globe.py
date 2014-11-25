__author__ = 'mike'

class Globe(object):
    light_on_state = False
    color = {'hue': 0, 'saturation': 0, 'brightness': 0}

    def __init__(self, light_response):
        self.set_color(light_response['color'])
        self.set_light_on_state(light_response['on'])

    def set_color(self, color):
        print color
        self.color = color

    def get_color(self):
        return self.color

    def set_light_on_state(self, state):
        self.light_on_state = state

    def get_light_on_state(self, state):
        return self.light_on_state

