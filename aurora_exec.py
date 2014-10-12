#!/usr/bin/python

from Aurora import Aurora
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
		aurora = Aurora()
 		aurora.set_alarm()
		while aurora.keep_running == True:
# 			print 'loop'
			time.sleep(10)
# 			print_next_alarm(aurora)
	# 	aurora.shutdown()
		# Main loop
	# 	while True:
	# 		print 'sleeping: ', datetime.datetime.now().time()
	# 		time.sleep(10) # Remember that the set_alarm() returns almost instantly, so the sleep should probably be
	# 		print 'set up:   ', datetime.datetime.now().time()
	# 		aurora.set_alarm(aurora.next_alarm)
	
	except KeyboardInterrupt:
		aurora.shutdown()
		print '#' * 10 + ' Exiting ' + '#' * 10
