from unittest import TestCase
from datetime import datetime, timedelta

from alarm import Alarm

__author__ = 'mike'


class TestAlarm(TestCase):
    def test_properties_are_set_by_constructor(self):
        end = datetime.now()
        duration = timedelta(minutes=15)

        dawn = {'end_time': end, 'duration': duration}
        sunrise = {'end_time': end, 'duration': duration}
        day = {'end_time': end}

        alarm = Alarm(dawn, sunrise, day)

        self.assertEquals(end, alarm.dawn['end_time'])
        self.assertEquals(duration, alarm.dawn['duration'])

        self.assertEquals(end, alarm.sunrise['end_time'])
        self.assertEquals(duration, alarm.sunrise['duration'])

        self.assertEquals(end, alarm.day['end_time'])