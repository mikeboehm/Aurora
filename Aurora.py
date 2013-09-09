#!/usr/bin/python

import datetime
import time
#import console
import sys
import math

import os
os.system('clear')

print '=' * 50
print ' ' * 22 + 'Aurora'
print '=' * 50
now = datetime.datetime.now()
# monday_alarm = datetime.time(7,0,0)
monday_alarm = datetime.datetime.now() + datetime.timedelta(hours=1,
minutes=0, seconds=2)

dawn_duration = datetime.timedelta(hours=1)
shutoff_delay = datetime.timedelta(hours=1)

today_alarm = datetime.datetime(now.year, now.month, now.day,
monday_alarm.hour, monday_alarm.minute, monday_alarm.second)
shutoff = today_alarm + shutoff_delay
dawn_begin = today_alarm - dawn_duration


print 'Alarm \t' + str(today_alarm)
print 'Now \t' + str(now)

# Determines the colour of the lights
def light_colour(seconds_in, dawn_duration):
	#	print dawn_duration
	print seconds_in / dawn_duration / 256
	# Determines whether we're in dawn mode

def is_alarm_happening(now, today_alarm, dawn_begin, dawn_duration):
	diff = now - dawn_begin
	#	print math.floor(diff.total_seconds())
	
	if now >= dawn_begin and now <= today_alarm:
		light_colour(math.floor(diff.total_seconds()), dawn_duration.total_seconds())
		message = 'Alarm is happening!'
	elif now <= dawn_begin:
		message = 'Still to come'
	else:
		message = 'Already happened'

# Main loop
a = 0
while a < 5:
	a = a + 1
	now = datetime.datetime.now()
	is_alarm_happening(now, today_alarm, dawn_begin, dawn_duration)
	time.sleep(1)