#!/usr/bin/python

for x in range(0, 10000):
	y = float(x)
	myvar = y/3
	
	if int(myvar % 3) != 0:
		print str(myvar) + ' ' + str(round(myvar, 2))
