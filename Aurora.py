#!/usr/bin/python

import datetime
import time
#import console
import sys
import math
import AuroraSunrise
import AuroraLights
import RPi.GPIO as GPIO

import os
os.system('clear')


### GPIO Hardware Pins ###
#	1	3.3v
#	3	SDA0		I2C	Data pin (SDA)
#	5	SCL0		I2C Clock	(SCL)
#	11	GPIO 0		Button/Switch
#	14	GND

###	PMW channels ###
# 	4		Red Pin
# 	5		Green Pin
# 	6		Blue Pin


# Setup GPIO for reading light button
GPIO.setmode(GPIO.BCM)  # Set's GPIO pins to BCM GPIO numbering
BUTTON_1 = 17           # Sets our input pins
GPIO.setup(BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set our input pin to be an input, with internal pullup resistor on

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
print 'dawn: ' + str(today_dawn)
print 'sunrise: ' + str(today_sunrise)
print 'shutoff: ' + str(today_shutoff)


# Set bounce time to be higher than the time it takes for the callback to return
# http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=40891
GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=lights.toggle_light_callback, bouncetime=3000)
# time.sleep(60)
	
# Main loop
a = 0
while True:
	a += 1
# 	lights.toggle_light()
	
	
	progress = sunrise.stage()
	print progress
	if progress:
		lights.set_sunrise_colour(progress)
		time.sleep(0.5)
	else: 
		time.sleep(1)
