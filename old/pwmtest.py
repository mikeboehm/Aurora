#!/usr/bin/python

import time
from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40, debug=True)
freq = 10
pwm.setPWMFreq(freq)
red_pin = 4
green_pin = 5
blue_pin = 6
pwm.setPWM(red_pin, 0 , 0)
pwm.setPWM(green_pin, 0 , 0)
pwm.setPWM(blue_pin, 0 , 0)


# pwm.setPWM(red_pin, 0 , 1000)
# time.sleep(1)
# pwm.setPWM(red_pin, 0 , 0)
# pwm.setPWM(green_pin, 0 , 1000)
# 
# time.sleep(1)
# pwm.setPWM(green_pin, 0 , 0)
# pwm.setPWM(red_pin, 0 , 4095)
# 
# time.sleep(1)
# pwm.setPWM(red_pin, 0 , 0)
# pwm.setPWM(green_pin, 0 , 1000)
# 
# time.sleep(1)
# pwm.setPWM(red_pin, 0 , 4096)
# pwm.setPWM(green_pin, 0 , 0)
# 
# time.sleep(1)
# pwm.setPWM(red_pin, 0 , 0)
# pwm.setPWM(green_pin, 0 , 1000)
# 
# time.sleep(1)
# pwm.setPWM(green_pin, 0 , 0)
start_time = time.time()
for x in range(0,4097, 16):
	my_var = x
	if x > 4095:
		my_var = 4095
	print my_var
	pwm.setPWM(red_pin, 0 , my_var)
	pwm.setPWM(green_pin, 0 , my_var)
	pwm.setPWM(blue_pin, 0 , my_var)

elapsed_time = time.time() - start_time

print elapsed_time


# for x in range(0,4095, 16):
# 	pwm.setPWM(red_pin, 0 , x)
# 	print x
# 	time.sleep(0.1)
# 	
# pwm.setPWM(green_pin, 0 , 1000)
# time.sleep(0.2)
# pwm.setPWM(green_pin, 0 , 1000)
# time.sleep(0.2)
# pwm.setPWM(green_pin, 0 , 1000)
# time.sleep(0.2)
# pwm.setPWM(green_pin, 0 , 1000)
# time.sleep(0.2)
# pwm.setPWM(green_pin, 0 , 0)