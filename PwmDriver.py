from Adafruit_PWM_Servo_Driver import PWM

class PwmDriver(object):
    RED_PIN = 1
    GREEN_PIN = 2
    BLUE_PIN = 3

    def __init__(self):
        # PWM config
        self.pwm = PWM(0x40, debug=False)
        self.freq = 10
        self.pwm.setPWMFreq(self.freq)

    def set_lights(self, red, green, blue):
        self.pwm.setPWM(self.RED_PIN, 0 , red)
        self.pwm.setPWM(self.GREEN_PIN, 0, green)
        self.pwm.setPWM(self.BLUE_PIN, 0, blue)
