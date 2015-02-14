__author__ = 'mike'

from datetime import date, timedelta, time, datetime


class AlarmModel(object):
    DAWN_DURATION = timedelta(minutes=15)
    SUNRISE_DURATION = timedelta(minutes=15)
    DAY_DURATION = timedelta(hours=2)

    sunrise = None
    date = None

    def __init__(self, hour, minutes, weekday):
        self.date = self.date_of_next_weekday(weekday)

        time_ = time(hour, minutes)
        self.sunrise = datetime.combine(self.date, time_)

    def get_sunrise(self):
        return self.sunrise

    def get_dawn(self, dawn_duration):
        sunrise = self.get_sunrise()
        return sunrise - dawn_duration

    def get_day_end(self, duration):
        sunrise = self.get_sunrise()
        return sunrise + duration

    def get_sunrise_start(self, sunrise_duration):
        sunrise = self.get_sunrise()

        return sunrise - (sunrise_duration/2)

    @staticmethod
    def date_of_next_weekday(weekday):
        day = date.today()
        for x in xrange(7):
            if day.weekday() == weekday:
                return day
            day += timedelta(days=1)