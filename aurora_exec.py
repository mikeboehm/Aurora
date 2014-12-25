#!/usr/bin/python

from Aurora import Aurora
from ButtonController import ButtonController
from Lights import Lights
from Settings import Settings
from JsonClient import JsonClient
# from PwmDriver import PwmDriver
from LifxClient import LifxClient
from Lifx import Lifx
import time
import os
import requests
os.system('clear')
os.system('nohup /usr/local/bin/ruby /usr/local/bin/lifx-http >> /home/pi/code/Aurora/lifx-cron-log.log &');

def print_next_alarm(aurora):
    time.sleep(2)
    next_alarm = aurora.get_next_alarm()
# 	print '&' * 30
# 	print 'GOT NEXT ALARM: ', next_alarm
# 	print '&' * 30

log_name = 'Aurora'
BUTTON_PIN = 17


if __name__ == '__main__':
    try:
        request = requests
        lifx_client = LifxClient(request)
        lifx = Lifx(lifx_client)


#         pwm_driver = PwmDriver()
        lights = Lights(lifx)

        jsonClient = JsonClient()
        settings = Settings(jsonClient)

        button_controller = ButtonController(BUTTON_PIN)

        aurora = Aurora(lights, settings, lifx, button_controller)

        aurora.set_alarm()
        while aurora.keep_running == True:
# 			print 'loop'
            time.sleep(10)

    except KeyboardInterrupt:
        print '#' * 10 + ' Exiting ' + '#' * 10
        aurora.shutdown()
        
