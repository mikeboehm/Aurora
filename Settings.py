import socket
from time import sleep

from basic_logger import Logger


class Settings(object):
    def __init__(self, JsonClient):
        self.JsonClient = JsonClient

        self.logger = Logger('Settings')

        hostname = self.get_hostname()
        port = 5000
        path = '/get_settings'
        self.url = "http://%s:%d%s" % (hostname, port, path)

        self.retry_count = 0

        self.settings = self.refresh_settings()

    def get_settings(self):
        self.logger.log('get_settings')
        return self.settings

    def set_settings(self, settings):
        self.logger.log('set_settings')
        self.settings = settings

    def refresh_settings(self):
        self.logger.log('refresh_settings')
        settings = self.get_settings_from_json()

        while not settings:
            print 'RETRY' * 20
            sleep(1)
            settings = self.get_settings_from_json()

        self.set_settings(settings)
        return settings

    def get_settings_from_json(self):
        self.logger.log('get_settings_from_json')
        try:
            settings = self.JsonClient.get(self.url)
        except IOError:
            settings = False
        return settings

    def get_alarms(self):
        self.logger.log('get_alarms')
        settings = self.get_settings()
        return settings['settings']['alarms']

    def get_alarm_for_day(self, day_number):
        self.logger.log('get_alarm_for_day')
        alarms = self.get_alarms()
        day_number_string = str(day_number)

        alarm_string = alarms[day_number_string]['time']

        return self.parse_time_string(alarm_string)

    @staticmethod
    def parse_time_string(string):
        alarm = string.split(':')

        hour = int(alarm[0])
        minutes = int(alarm[1])

        return {'hour': hour, 'minutes': minutes}

    def get_hostname(self):
        self.logger.log('get_hostname')
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