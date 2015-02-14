### GPIO Hardware Pins ###
#   1   3.3v
#   3   SDA0        I2C Data pin (SDA)
#   5   SCL0        I2C Clock   (SCL)
#   14  GND

### PWM PINS ###
#   1   Red
#   2   Green
#   3   Blue

### PMW channels ###
#   4       Red Pin
#   5       Green Pin
#   6       Blue Pin


from threading import Thread
import datetime
import math
import time

from Adafruit_PWM_Servo_Driver import PWM


class PwmDriver(object):
    DAWN_END_COLOR = {'red': 4095, 'green': 0, 'blue': 0}
    SUNRISE_END_COLOR = {'red': 4095, 'green': 4095, 'blue': 4095}
    SHUTOFF_COLOR = {'red': 0, 'green': 0, 'blue': 0}


    black = {'red': 0, 'green': 0, 'blue': 0}
    fade_end_colour = black

    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin

        # PWM config
        self.pwm = PWM(0x40, debug=False)
        self.freq = 10
        self.pwm.setPWMFreq(self.freq)

        self.current_colour = self.black

        # Set "current_colour" and PWM to black/off
        self.set_lights(self.current_colour)

        # Setup fade values
        end_time = datetime.datetime.now()
        self.fade_end_time = end_time

        self.fade_diffs_dict = self.fade_diffs(self.black, self.black)
        self.fade_total_duration = datetime.timedelta(seconds=0)

        # Create fade loops so we can test if they're running and also kill them
        self.fade_loop = Thread(target=self.fader)

        # Reading light settings
        self.light_state = False

        reading_light = {'red': 255, 'green': 25, 'blue': 0}
        # Convert 8-bit colour to 12-bit (for PWM)
        self.reading_light = {
            'red': reading_light['red'] * 16,
            'green': reading_light['green'] * 16,
            'blue': reading_light['blue'] * 16
        }
        self.reading_light_duration = datetime.timedelta(seconds=1)

    # Turns reading lights off
    def lights_off(self):
        end_colour = {'red': 0, 'green': 0, 'blue': 0}
        fade = {'duration': self.reading_light_duration, 'end_colour': end_colour}

        self.set_fade(fade)

    # Turns reading lights on
    def lights_on(self):
        fade = {'duration': self.reading_light_duration, 'end_colour': self.reading_light}

        self.set_fade(fade)

    def toggle_lights(self):
        if self.light_state:
            self.lights_off()
            self.light_state = False
        else:
            self.lights_on()
            self.light_state = True

    def dawn(self, duration):
        fade = {'end_colour': self.DAWN_END_COLOR, 'duration': duration}
        self.set_fade(fade)

    def sunrise(self, duration):
        fade = {'end_colour': self.SUNRISE_END_COLOR, 'duration': duration}
        self.set_fade(fade)

    def shutoff(self, duration):
        fade = {'end_colour': self.SHUTOFF_COLOR, 'duration': duration}
        self.set_fade(fade)

    # Set threaded fade
    def set_fade(self, fade):
        duration = fade['duration']
        end_colour = fade['end_colour']

        self.fade_end_time = datetime.datetime.now() + duration
        self.fade_end_colour = end_colour
        # Get current light colour
        current_colour = self.get_lights()

        # Get colours differences
        self.fade_diffs_dict = self.fade_diffs(current_colour, end_colour)

        # Convert seconds into microsecnds
        total_duration = duration.seconds * 1000000
        self.fade_total_duration = float(total_duration)

        # Start fade loop
        self.fade_loop = Thread(target=self.fader)
        self.fade_loop.start()

    def get_lights(self):
        return self.current_colour

    # Returns a dict of the difference between two colours
    def fade_diffs(self, start_colour, end_colour):
        diff_red = self.fade_diff(end_colour['red'], start_colour['red'])
        diff_green = self.fade_diff(end_colour['green'], start_colour['green'])
        diff_blue = self.fade_diff(end_colour['blue'], start_colour['blue'])

        return {'red': diff_red, 'green': diff_green, 'blue': diff_blue}

    # Calculate the difference between two tints
    def fade_diff(self, start_colour, end_colour):
        diff = (end_colour - start_colour) / 100.00
        diff_absolute = math.fabs(diff)

        return {'diff': diff, 'absolute': diff_absolute}

    def set_lights(self, colour):
        red = int(colour['red'])
        green = int(colour['green'])
        blue = int(colour['blue'])

        self.pwm.setPWM(self.red_pin, 0, red)
        self.pwm.setPWM(self.green_pin, 0, green)
        self.pwm.setPWM(self.blue_pin, 0, blue)

        self.current_colour = {'red': red, 'green': green, 'blue': blue}

    # Returns the values that set_fade sets
    def get_fade(self):
        return {
            'fade_end_time': self.fade_end_time,
            'fade_total_duration': self.fade_total_duration,
            'fade_diffs_dict': self.fade_diffs_dict,
            'fade_end_colour': self.fade_end_colour
        }

    def fader(self):
        # While now is <= fade end
        # Fade
        while datetime.datetime.now() <= self.fade_end_time:
            current_lights = self.get_lights()
            # time till end = end_time - now
            diff = self.fade_end_time - datetime.datetime.now()
            remaining = (diff.seconds * 1000000) + diff.microseconds
            percent_remaining = round((remaining / self.fade_total_duration) * 100, 2)

            colour = self.fade_colours(self.fade_diffs_dict, percent_remaining, current_lights)
            self.set_lights(colour)

            time.sleep(0.0001)

        self.set_lights(self.fade_end_colour)

    # Returns colour to be set, based on the colour diffs
    def fade_colours(self, diffs, percent_remaining, current_lights):
        # Calculate values
        red = self.fade_colour(diffs['red'], percent_remaining, current_lights['red'])
        green = self.fade_colour(diffs['green'], percent_remaining, current_lights['green'])
        blue = self.fade_colour(diffs['blue'], percent_remaining, current_lights['blue'])

        return {'red': red, 'green': green, 'blue': blue}

    # Child method of fade_colours()
    def fade_colour(self, colour, percent_remaining, current_colour):
        if colour['diff'] < 0:
            colour_to_set = (100 - percent_remaining) * colour['absolute']
        elif colour['diff'] == 0:
            colour_to_set = current_colour
        else:
            colour_to_set = percent_remaining * colour['absolute']

        return colour_to_set