__author__ = 'mike'


class Alarm(object):
    dawn = {}
    sunrise = {}
    day = {}

    def __init__(self, dawn, sunrise, day):
        self.dawn = dawn
        self.sunrise = sunrise
        self.day = day

