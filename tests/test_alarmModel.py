from unittest import TestCase
from datetime import datetime, date, timedelta, time

from alarm_model import AlarmModel

__author__ = 'mike'


class TestAlarmModel(TestCase):
    def setUp(self):
        pass

    def test_date_of_next_weekday(self):
        # Today
        today = date.today()
        result = AlarmModel.date_of_next_weekday(today.weekday())
        self.assertEqual(today, result)

        # Tomorrow
        tomorrow = date.today() + timedelta(days=1)
        result = AlarmModel.date_of_next_weekday(tomorrow.weekday())
        self.assertEqual(tomorrow, result)

        # Six days from now
        six_days_from_now = date.today() + timedelta(days=6)
        result = AlarmModel.date_of_next_weekday(six_days_from_now.weekday())
        self.assertEqual(six_days_from_now, result)

    def test_it_gets_time_of_sunrise(self):
        hours = 7
        minutes = 31
        today = date.today()
        expected = datetime.combine(date.today(), time(hours, minutes))
        alarm_model = AlarmModel(hours, minutes, today.weekday())
        result = alarm_model.get_sunrise()

        self.assertEqual(expected, result)

    def test_it_gets_time_of_dawn(self):
        now = datetime.now()

        duration = timedelta(minutes=30)
        expected = datetime(
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute
        ) - duration

        alarm_model = AlarmModel(now.hour, now.minute, now.weekday())

        result = alarm_model.get_dawn(duration)

        self.assertEqual(expected, result)

    def test_it_gets_auto_shutoff_time(self):
        now = datetime.now()

        duration = timedelta(minutes=30)
        expected = datetime(
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute
        ) + duration

        alarm_model = AlarmModel(now.hour, now.minute, now.weekday())

        result = alarm_model.get_day_end(duration)

        self.assertEqual(expected, result)

    def test_get_sunrise_start(self):
        now = datetime.now()

        duration = timedelta(minutes=30)
        expected = datetime(
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute
        ) - (duration/2)

        alarm_model = AlarmModel(now.hour, now.minute, now.weekday())

        result = alarm_model.get_sunrise_start(duration)

        self.assertEqual(expected, result)