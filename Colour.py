class Colour(object):
    hue = 0
    saturation = 0.0
    brightness = 0.0
    kelvin = 2600
    KELVIN_MIN = 2500
    KELVIN_MAX = 9000


    def __init__(self, colour=False):
        if colour:
            self.hue = int(colour['hue'])
            self.saturation = float(colour['saturation'])
            self.brightness = float(colour['brightness'])
            self.set_kelvin(colour['kelvin'])

    def set_kelvin(self, kelvin):
        kelvin = int(kelvin)
        if kelvin < self.KELVIN_MIN:
            self.kelvin = self.KELVIN_MIN
        elif kelvin > self.KELVIN_MAX:
            self.kelvin = self.KELVIN_MAX
