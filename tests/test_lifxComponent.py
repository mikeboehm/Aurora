from unittest import TestCase
from LifxComponent import LifxComponent
__author__ = 'mike'


class TestLifxComponent(TestCase):
    def setUp(self):
        self.lifx_component = LifxComponent()

    def test_toggle_reading_lights(self):
        self.assertFalse(self.lifx_component.reading_light_on)

        self.lifx_component.toggle_reading_lights()
        self.assertTrue(self.lifx_component.reading_light_on)