from Adafruit_PWM_Servo_Driver import PWM
import RPi.GPIO as GPIO

class GPIOController(object):
    RED_PIN = 1
    GREEN_PIN = 2
    BLUE_PIN = 3

    def __init__(self):
		# self.parent = parent

        # # Setup GPIO for reading light button
        # GPIO.setmode(GPIO.BCM)  # Set's GPIO pins to BCM GPIO numbering
        # self.BUTTON_1 = 17           # Sets our input pin
        # GPIO.setup(self.BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set our input pin to be an input, with internal pullup resistor on

        # Setup push-button callback
# 		GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=self.parent.toggle_light_callback, bouncetime=300)

        # PWM config
        self.pwm = PWM(0x40, debug=False)
        self.freq = 10
        self.pwm.setPWMFreq(self.freq)

    # def set_parent(self, parent):
    #     self.parent = parent
    #     # Setup push-button callback
    #     GPIO.add_event_detect(self.BUTTON_1, GPIO.FALLING, callback=self.parent.toggle_light_callback, bouncetime=300)

    def set_lights(self, red, green, blue):
        self.pwm.setPWM(self.RED_PIN, 0 , red)
        self.pwm.setPWM(self.GREEN_PIN, 0, green)
        self.pwm.setPWM(self.BLUE_PIN, 0, blue)
