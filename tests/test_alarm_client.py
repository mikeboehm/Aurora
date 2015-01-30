from datetime import datetime, timedelta
from mock import MagicMock
from unittest import TestCase

from alarm_client import AlarmClient
from alarm_model import AlarmModel

__author__ = 'mike'


class TestAlarmClient(TestCase):
    alarm_client = None
    # alarm_time = datetime.now()
    monday = {'hour': 7, 'minutes': 0}
    tuesday = {'hour': 7, 'minutes': 0}
    wednesday = {'hour': 7, 'minutes': 0}
    thursday = {'hour': 7, 'minutes': 0}
    friday = {'hour': 7, 'minutes': 0}
    saturday = {'hour': 7, 'minutes': 0}
    sunday = {'hour': 7, 'minutes': 0}

    alarm_settings = {
        0: monday,
        1: tuesday,
        2: wednesday,
        3: thursday,
        4: friday,
        5: saturday,
        6: sunday
    }

    # settings = {'alarms': {1: {'time': monday}}}

    def setUp(self):
        settings = MagicMock()
        settings.get_alarms = MagicMock(return_value=self.alarm_settings)
        self.alarm_client = AlarmClient(settings)

    def test_it_hydrates_an_alarm_model(self):
        now = datetime.now()
        alarm = {'hour': 1, 'minutes': 23}
        expected = AlarmModel(alarm['hour'], alarm['minutes'], now.weekday())
        result = self.alarm_client.hydrate_alarm_model(alarm, now.weekday())

        self.assertEqual(expected.get_sunrise(), result.get_sunrise())

    def test_it_gets_alarm_for_given_day(self):
        weekday = 2
        expected = AlarmModel(self.alarm_settings[weekday]['hour'], self.alarm_settings[weekday]['minutes'], weekday)
        result = self.alarm_client.get_alarm_for_weekday(2)

        self.assertEquals(expected.get_sunrise(), result.get_sunrise())

    def test_it_gets_alarm_for_today(self):
        today = datetime.now().weekday()

        expected = AlarmModel(self.alarm_settings[today]['hour'], self.alarm_settings[today]['minutes'], today).get_sunrise()
        result = self.alarm_client.get_today_alarm().get_sunrise()

        self.assertEquals(expected, result)

    def test_it_gets_next_alarm(self):
        now = datetime.now()


    def test_it_returns_seconds_till_given_time(self):
        pass

    def test_it_creates_a_timer_thread(self):
        pass

    def test_when_timer_expires_it_executes_callback(self):
        pass