__author__ = 'mike'

from LifxClient import LifxClient


class Lifx(object):
    PRE_DAWN = {
        'hue': 0,
        'saturation': 1,
        'brightness': 0,
        'kelvin': 2500
    }

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

    PRE_READING_LIGHT = {
        'hue': 0,
        'saturation': 1,
        'brightness': 0,
        'kelvin': 2500
    }

    READING_LIGHT = {
        'hue': 0,
        'saturation': 1,
        'brightness': 0.25,
        'kelvin': 2500
    }

    current_color = {
            'hue': 0,
            'saturation': 1,
            'brightness': 0.25,
            'kelvin': 2500
    }

    pre_fade_duration = 1

    def __init__(self, lifx_client):
        """
        :type lifx_client: LifxClient
        """
        self.client = lifx_client

    def dawn(self, dawn_duration):
        self.client.fade(self.PRE_DAWN, self.pre_fade_duration)
        self.client.fade(self.DAWN, dawn_duration)

    def sunrise(self, sunrise_duration):
        self.client.fade(self.DAY, sunrise_duration)

    def shutoff(self, shutoff_speed):
        self.client.fade(self.PRE_READING_LIGHT, shutoff_speed)
        self.client.turn_off()
    
    def reading_lights_on(self):
        self.client.fade(self.READING_LIGHT, self.pre_fade_duration)
        response = self.client.turn_on()
        if response:
            return True

    def reading_lights_off(self):
        response = self.client.turn_off()
        if response:
            return True

    def reading_lights_toggle(self):
        response = self.client.toggle()
        if response:
            return True