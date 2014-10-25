#!/usr/bin/python

from Aurora import Aurora
from Lights import Lights
from Settings import Settings
import time
import os
os.system('clear')

def print_next_alarm(aurora):
	time.sleep(2)
	next_alarm = aurora.get_next_alarm()
# 	print '&' * 30
# 	print 'GOT NEXT ALARM: ', next_alarm
# 	print '&' * 30


if __name__ == '__main__':
	try:
		lights = Lights()
		settings = Settings()
		aurora = Aurora(lights)
 		aurora.set_alarm()
		while aurora.keep_running == True:
# 			print 'loop'
			time.sleep(10)
	
	except KeyboardInterrupt:
		aurora.shutdown()
		print '#' * 10 + ' Exiting ' + '#' * 10
