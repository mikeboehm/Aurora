from unittest import TestCase
import requests
from Lifx import Lifx
from LifxClient import LifxClient

__author__ = 'mike'


class TestLifx(TestCase):
    def setUp(self):
        lifx_client = LifxClient(requests)
        self.lifx = Lifx(lifx_client)

    def test_dawn(self):
        self.fail()

    def test_sunrise(self):
        self.fail()

    def test_shutoff(self):
        self.fail()

    def test_readinglights_on(self):
        self.fail()

    def test_readinglights_off(self):
        self.fail()

    def test_readinglights_toggle(self):
        response = self.lifx.readinglights_toggle()
        self.assertTrue(response)
