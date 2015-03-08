
import Lifx


class Lights(object):
    DAWN_END_COLOR = {'red': 4095, 'green': 0, 'blue': 0}
    SUNRISE_END_COLOR = {'red': 4095, 'green': 4095, 'blue': 4095}
    SHUTOFF_COLOR = {'red': 0, 'green': 0, 'blue': 0}

    logger = None

    def __init__(self, lifx_controller, logger):
        """
        :type lifx_controller: Lifx.Lifx
        """

        self.light_adapter = lifx_controller

        self.logger = logger
        self._log('init()')

    # Turns reading lights off
    def lights_off(self):
        self._log('lights_off()')
        self.light_adapter.reading_lights_off()

    # Turns reading lights on
    def lights_on(self):
        self._log('lights_on()')
        self.light_adapter.reading_lights_on()

    def toggle_lights(self):
        self._log('toggle_lights()')
        print 'Toggle lights'
        self.light_adapter.reading_lights_toggle()

    def dawn(self, duration):
        self._log('dawn()')

        self.light_adapter.dawn(duration)

    def sunrise(self, duration):
        self._log('sunrise()')
        self.light_adapter.sunrise(duration)

    def shutoff(self, duration):
        self._log('shutoff()')
        self.light_adapter.shutoff(duration)

    def _log(self, method_name, message=None):
        log_line = str(method_name)

        if message:
            log_line += ': ' + str(message)

        self.logger.write(log_line, 'Lights')