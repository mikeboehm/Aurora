import socket
from time import sleep


class Settings(object):
    def __init__(self, JsonClient, Logger):
        self.JsonClient = JsonClient

        self.logger = Logger

        hostname = self.get_hostname()
        port = 5000
        path = '/get_settings'
        self.url = "http://%s:%d%s" % (hostname, port, path)

        self.retry_count = 0

        self.settings = self.refresh_settings()

    def get_settings(self):
        self._log('get_settings()')
        return self.settings

    def set_settings(self, settings):
        self._log('set_settings()')
        self.settings = settings

    def refresh_settings(self):
        self._log('refresh_settings()')
        settings = self.get_settings_from_json()

        while not settings:
            print 'RETRY'
            sleep(1)
            settings = self.get_settings_from_json()

        self.set_settings(settings)
        return settings

    # Used
    def get_settings_from_json(self):
        self._log('get_settings_from_json()')
        try:
            settings = self.JsonClient.get(self.url)
        except IOError:
            settings = False
        return settings

    # Will be used
    def get_alarms(self):
        self._log('get_alarms()')
        settings = self.get_settings()
        return settings['settings']['alarms']

    def get_alarm_for_day(self, day_number):
        self._log('get_alarm_for_day()')
        alarms = self.get_alarms()
        day_number_string = str(day_number)

        alarm_string = alarms[day_number_string]['time']

        return self.parse_time_string(alarm_string)

    def parse_time_string(self, string):
        self._log('parse_time_string()')
        alarm = string.split(':')

        hour = int(alarm[0])
        minutes = int(alarm[1])

        return {'hour': hour, 'minutes': minutes}

    def get_hostname(self):
        self._log('get_hostname()')
        # Generate hostname
        bonjour_address = socket.gethostname()
        # If IP address, use as is
        try:
            socket.inet_aton(bonjour_address)
        except socket.error:
            # Otherwise make sure the address will work
            if not bonjour_address.endswith('.local'):
                bonjour_address += '.local'

        return bonjour_address

    def _log(self, method_name, message=None):
        log_line = str(method_name)

        if message:
            log_line += ': ' + str(message)

        self.logger.write(log_line, 'Settings')