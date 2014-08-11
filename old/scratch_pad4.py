#!/usr/bin/python

import datetime

# Settings
sunrise_monday 		= datetime.time(7,0,0)
sunrise_tuesday 	= datetime.time(7,0,0)
sunrise_wednesday 	= datetime.time(7,0,0)
sunrise_thursday 	= datetime.time(7,15,0)
sunrise_friday 		= datetime.time(7,10,0)
sunrise_saturday 	= datetime.time(9,55,0)
sunrise_sunday 		= datetime.time(10,30,0)

sunrise_times = { 1 : sunrise_monday, 2 : sunrise_tuesday, 3 : sunrise_wednesday, 4 : sunrise_thursday, 5 : sunrise_friday, 6 : sunrise_saturday, 7 : sunrise_sunday}

print sunrise_times[1].hour

now = datetime
current_hour = now.datetime.now().hour
current_minute = now.datetime.now().minute
current_second = now.datetime.now().second
# print now.date()
# current_day_number = now.date.isoweekday()

print current_hour
print current_minute
print current_second


current_time = datetime.datetime.now()
today_iso_weekday_number = current_time.isoweekday()
print current_time.minute
current_hour = datetime.datetime.now().hour
current_minute = datetime.datetime.now().minute
current_second = datetime.datetime.now().second
print sunrise_monday.hour
# print dir(datetime.datetime.now())
# print vars(datetime.datetime.now())

	
sunrise_time = sunrise_times[today_iso_weekday_number]
print sunrise_time.hour

if current_time < sunrise_time:
	print "Before sunrise"
elif sunrise_time >= current_time:
	print "After sunrise"