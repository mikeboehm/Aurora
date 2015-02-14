
import Lifx


class Lights(object):
    DAWN_END_COLOR = {'red': 4095, 'green': 0, 'blue': 0}
    SUNRISE_END_COLOR = {'red': 4095, 'green': 4095, 'blue': 4095}
    SHUTOFF_COLOR = {'red': 0, 'green': 0, 'blue': 0}

    logger = None

    def __init__(self, lifx_controller, pwm_driver, logger):
        """
        :type lifx_controller: Lifx.Lifx
        """
        self.pwm_driver = pwm_driver
        self.lifx_controller = lifx_controller

        self.logger = logger
        self._log('init')

    # Turns reading lights off
    def lights_off(self):
        self._log('lights_off')
        self.lifx_controller.reading_lights_off()
        self.pwm_driver.lights_off()

    # Turns reading lights on
    def lights_on(self):
        self._log('lights_on')
        self.lifx_controller.reading_lights_on()
        self.pwm_driver.lights_on()

    def toggle_lights(self):
        self._log('toggle_lights')
        print 'Toggle lights'
        self.lifx_controller.reading_lights_toggle()
        self.pwm_driver.toggle_lights()

    def dawn(self, duration):
        self._log('dawn')

        self.lifx_controller.dawn(duration)
        self.pwm_driver.dawn(duration)

    def sunrise(self, duration):
        self._log('sunrise')
        self.lifx_controller.sunrise(duration)
        self.pwm_driver.sunrise(duration)

    def shutoff(self, duration):
        self._log('shutoff')
        self.lifx_controller.shutoff(duration)
        self.pwm_driver.shutoff(duration)

    def _log(self, method_name, message=None):
        log_line = method_name + '()'

        if message:
            log_line += ': ' + str(message)

        self.logger.write(log_line, 'Lights')