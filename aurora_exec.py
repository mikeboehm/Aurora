#!/usr/bin/python

from Aurora import Aurora
from ButtonController import ButtonController
from MockButtonController import MockButtonController
from Lights import Lights
from Settings import Settings
from JsonClient import JsonClient
from LifxClient import LifxClient
from Lifx import Lifx
from basic_logger import Logger
import time
import os
import requests

location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

os.system('clear')
os.system('sudo nohup /usr/local/bin/lifx-http >> ' + location + '/logs/lifx-http.log &')

BUTTON_PIN = 17

if __name__ == '__main__':
    try:
        logger = Logger()

        request = requests
        lifx_client = LifxClient(request, logger)
        lifx = Lifx(lifx_client, logger)

        lights = Lights(lifx, logger)

        jsonClient = JsonClient()
        settings = Settings(jsonClient)

        button_controller = ButtonController(BUTTON_PIN)
        # mock_button_controller = MockButtonController()

        aurora = Aurora(
            lights,
            settings,
            button_controller,
            logger
        )

        aurora.set_alarm()
        while aurora.keep_running == True:
# 			print 'loop'
            time.sleep(10)

    except KeyboardInterrupt:
        print '#' * 10 + ' Exiting ' + '#' * 10
        aurora.shutdown()

