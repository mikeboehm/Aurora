from unittest import TestCase
from Colour import Colour
__author__ = 'mike'


class TestColour(TestCase):
    def test_hue_is_int(self):
        colour_dict = {
            'hue': 120.0,
            'saturation': 0.0,
            'brightness': 0.0,
            'kelvin': 0.0
        }
        colour = Colour(colour_dict)
        self.assertIsInstance(colour.hue, int)

    def test_saturation_is_float(self):
        colour_dict = {
            'hue': 120.0,
            'saturation': 1,
            'brightness': 0.0,
            'kelvin': 0.0
        }
        colour = Colour(colour_dict)
        self.assertIsInstance(colour.saturation, float)

    def test_brightness_is_float(self):
        colour_dict = {
            'hue': 120.0,
            'saturation': 1,
            'brightness': 1,
            'kelvin': 0.0
        }
        colour = Colour(colour_dict)
        self.assertIsInstance(colour.brightness, float)

    def test_kelvin_is_within_range_and_int(self):
        colour_dict = {
            'hue': 120.0,
            'saturation': 1,
            'brightness': 1,
            'kelvin': 0.0
        }
        colour = Colour(colour_dict)
        self.assertIsInstance(colour.brightness, float)
        self.assertLessEqual(colour.KELVIN_MIN, colour.kelvin)
        self.assertGreaterEqual(colour.KELVIN_MAX, colour.kelvin)