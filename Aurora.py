#!/usr/bin/python

import datetime
import time
#import console
import sys
import math
import AuroraSunrise
import AuroraLights

import os
os.system('clear')

print '=' * 50
print ' ' * 22 + 'Aurora'
print '=' * 50
now = datetime.datetime.now()
# monday_alarm = datetime.time(7,0,0)
monday_alarm = datetime.datetime.now() + datetime.timedelta(hours=1, minutes=0, seconds=2)

dawn_duration = datetime.timedelta(hours=1)
shutoff_delay = datetime.timedelta(hours=1)

today_alarm = datetime.datetime(now.year, now.month, now.day, monday_alarm.hour, monday_alarm.minute, monday_alarm.second)
shutoff = today_alarm + shutoff_delay
dawn_begin = today_alarm - dawn_duration


print 'Alarm \t' + str(today_alarm)
print 'Now \t' + str(now)

# Determines the colour of the lights
def light_colour(seconds_in, dawn_duration):
	#	print dawn_duration

# 	print seconds_in / dawn_duration
 	print seconds_in

def update_settings():
#	update settings
	pass


"""
	Alarm
		Do Alarm
		Update settings
		Timer thread with callback
	Lamp
		Toggle lamp
		Toggle state

"""

lights = AuroraLights.Lights()

sunrise = AuroraSunrise.Sunrise()

today_sunrise = sunrise.sunrise()
today_dawn = sunrise.dawn()
today_shutoff = sunrise.shutoff()
print '~' * 20
print today_dawn
print today_sunrise
print today_shutoff

	
# Main loop
a = 0
while a < 3000:
	a += 1
	progress = sunrise.stage()
	if progress:
		lights.set_sunrise_colour(progress)
	# if switch_pressed:
		# toggle light
	# if sunrising:
		# set_light
	# start_delay()
	
	time.sleep(1)
