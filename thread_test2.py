import time
from threading import Thread

class MyLilThread(object):
	def __init__(self):
		self.state = 'on';
	
	def my_lil_thread(self):
		for x in range(0, 20):
			print self.state
			time.sleep(0.5)
		

my_thread = MyLilThread()

t = Thread(target=my_thread.my_lil_thread)
t.start()

for x in range(0, 200):
	if(x % 5 == 0):
		print my_thread.state
		if my_thread.state == 'on':
			my_thread.state = 'off'
		else:
			my_thread.state = 'on'
	time.sleep(0.5)