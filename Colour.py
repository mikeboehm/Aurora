class Colour(object):
    hue = 0
    saturation = 0.0
    brightness = 0.0
    kelvin = 2600

    def __init__(self, colour=False):
        if colour:
            self.hue = colour['hue']
            self.saturation = colour['saturation']
            self.brightness = colour['brightness']
            self.kelvin = colour['kelvin']