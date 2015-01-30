__author__ = 'mike'

from datetime import datetime

from alarm_model import AlarmModel


class AlarmClient(object):
    settingsClient = None

    def __init__(self, settings_client):
        self.settingsClient = settings_client

    def get_alarms(self):
        return self.settingsClient.get_alarms()

    def get_today_alarm(self):
        today = datetime.now().weekday()
        return self.get_alarm_for_weekday(today)

    def get_alarm_for_weekday(self, weekday):
        alarms = self.get_alarms()
        weekday_setting = alarms[weekday]

        return self.create_alarm_model(weekday_setting['hour'], weekday_setting['minutes'], weekday)

    def hydrate_alarm_model(self, alarm, weekday):
        hour = alarm['hour']
        minutes = alarm['minutes']

        now = datetime.now()

        return self.create_alarm_model(hour, minutes, weekday)

    def create_alarm_model(self, hour, minutes, weekday):
        return AlarmModel(hour, minutes, weekday)