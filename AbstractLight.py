__author__ = 'mike'


class AbstractLight(object):
    reading_light_on = False

    def toggle_reading_lights(self):
        raise NotImplementedError( "toggle_reading_lights() needs to be implemented" )

    def trigger_dawn(self):
        raise NotImplementedError( "trigger_dawn() needs to be implemented" )

    def trigger_sunrise(self):
        raise NotImplementedError( "trigger_sunrise() needs to be implemented" )

    def trigger_end_of_day(self):
        raise NotImplementedError( "trigger_end_of_day() needs to be implemented" )
