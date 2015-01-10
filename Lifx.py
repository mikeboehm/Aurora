__author__ = 'mike'
from threading import Thread

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

    PRE_DAY = {
        'hue': 0,
        'saturation': 0,
        'brightness': 0,
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
        'hue': 29,
        'saturation': 1,
        'brightness': 0,
        'kelvin': 2500
    }
    
    READING_LIGHT = {
        'hue': 29,
        'saturation': 1,
        'brightness': 1,
        'kelvin': 2500
    }

    current_color = {
        'hue': 0,
        'saturation': 1,
        'brightness': 0.25,
        'kelvin': 2500
    }

    pre_fade_duration = 0
    reading_light_duration = 2
    client_thread = ''

    """
    :type lifx_client: LifxClient
    """
    def __init__(self, lifx_client):
        self.client = lifx_client
        self.client_thread = Thread()

    def dawn(self, dawn_duration):
        self.client.fade(self.PRE_DAWN, self.pre_fade_duration)
        self.client.turn_on()
        self.client.fade(self.DAWN, dawn_duration)

    def sunrise(self, sunrise_duration):
        self.client.fade(self.DAY, sunrise_duration)

    def shutoff(self, shutoff_speed):
        self.client.fade(self.PRE_DAY, shutoff_speed)
        self.client.turn_off()
        self.client.fade(self.PRE_READING_LIGHT, self.pre_fade_duration)        
    
    def reading_lights_on(self):
        self.client.fade(self.PRE_READING_LIGHT, self.pre_fade_duration)
        self.client.turn_on()
        self.client.fade(self.READING_LIGHT, self.reading_light_duration)

    def reading_lights_off(self):
        self.client.fade(self.PRE_READING_LIGHT, self.reading_light_duration)
        self.client.turn_off()

    def reading_lights_toggle(self):
        self.client_thread = Thread(target=self.client.toggle)
        # self.client.toggle()
        self.client_thread.start()
        
