# Code to execute in an independent thread
import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# Create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()
i = 0
while i < 120:
	print i
	i += 1
	if t.is_alive():
	    print('Still running')
	else:
	    print('Completed')
	time.sleep(0.1)
