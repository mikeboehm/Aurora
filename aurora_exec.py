#!/usr/bin/python

from Aurora import Aurora
from Lights import Lights
from Settings import Settings
from JsonClient import JsonClient
from PwmDriver import PwmDriver
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

if __name__ == '__main__':
    try:
        request = requests
        lifx_client = LifxClient(request)
        lifx = Lifx(lifx_client)


        pwm_driver = PwmDriver()
        lights = Lights(pwm_driver, lifx)

        jsonClient = JsonClient()
        settings = Settings(jsonClient)

        aurora = Aurora(lights, settings, lifx)

        aurora.set_alarm()
        while aurora.keep_running == True:
# 			print 'loop'
            time.sleep(10)

    except KeyboardInterrupt:
        aurora.shutdown()
        print '#' * 10 + ' Exiting ' + '#' * 10
