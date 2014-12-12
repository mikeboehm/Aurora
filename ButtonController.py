__author__ = 'mike'

import RPi.GPIO as GPIO


class ButtonController(object):

    parent = False
    parent_callback = False

    def __init__(self, button_pin=17):
        # Setup GPIO for reading light button
        GPIO.setmode(GPIO.BCM)  # Set's GPIO pins to BCM GPIO numbering
        self.BUTTON_1 = button_pin  # Sets our input pin

        # Set our input pin to be an input, with internal pullup resistor on
        GPIO.setup(self.BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Setup push-button callback
        GPIO.add_event_detect(self.BUTTON_1, GPIO.FALLING, callback=self.callback_method, bouncetime=300)

    def callback_method(self, channel):
        if self.parent and self.parent_callback:
            parent_callback = getattr(self.parent, self.parent_callback)
            parent_callback()

    def set_parent(self, parent, callback_method):
        """
        :param parent: string
        :param callback_method: string
        """
        self.parent = parent
        self.parent_callback = callback_method