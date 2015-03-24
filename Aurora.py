#!/usr/bin/python

import datetime
import threading

import pika

import Lifx
import Lights


# import RPi.GPIO as GPIO

# Glossary
# Dawn      is the first appearance of light in the sky before sunrise. The start of the first sequence (black to red)
# Twilight  is the period between dawn and sunrise
# Sunrise   is the time in the morning when the sun appears. The start of the second sequence (red to white)
# Day       occurs once the sunrise sequence is complete
# Daybreak  could be the term for the event at the end of sunrise?


class Aurora(object):
    SHUTOFF_DURATION = None

    """
    :type lights: Lights.Lights
    """
    lights = ''
    light_callback_method = 'toggle_light_callback'

    logger = None

    def __init__(self, lights, settings, gpio_controller, logger):
        """
        :param lights:
        :param gpio_controller:
        :type lights: Lights.Lights
        :param settings:
        :return:
        """
        self.lights = lights
        self.settings = settings
        self.next_alarm = False
        self.keep_running = True

        self.logger = logger
        self._log('init()')

        self.SHUTOFF_DURATION = datetime.timedelta(seconds=2)

        # Initialise alarm threads so we can test if they're running
        self.dawn_timer = threading.Timer(1, self.trigger_dawn)
        self.sunrise_timer = threading.Timer(1, self.trigger_sunrise)
        self.shutoff_thread = threading.Timer(1, self.trigger_autoshutoff)

        self.rabbit_listener_thread = threading.Thread(target=self.rabbit_listener)
        self.rabbit_listener_thread.start()

        gpio_controller.set_parent(self, self.light_callback_method)

    # Callback from push-button press to toggle reading lights
    def toggle_light_callback(self):
        self._log('toggle_light_callback()', 'Toggle light from button press')
        self.lights.toggle_lights()

    def rabbit_listener(self):
        self._log('rabbit_listener()')
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='aurora')

        print ' [*] Waiting for messages. To exit press CTRL+C'

        channel.basic_consume(
            self.rabbit_callback,
            queue='aurora',
            no_ack=True
        )

        channel.start_consuming()

    def rabbit_callback(self, ch, method, properties, body):
        self._log('rabbit_callback()', 'Message received from web app: "' + str(body) + '"')
        print " [x] Received %r" % (body,)
        self._log(body)
        self.toggle_light_callback()

    # Returns settings from config
    def get_settings(self):
        # Set next update thread
        pass

    # Creates a Timer thread for the next alarm
    def set_alarm(self):
        self._log('set_alarm()')
        # Get next alarm
        next_alarm = self.get_next_alarm()
        print 'Sunrise:', next_alarm['sunrise']['end_time']
        self._log('Sunrise:' + str(next_alarm['sunrise']['end_time']))

        dawn = next_alarm['dawn']['end_time'] - next_alarm['dawn']['duration']
        seconds_to_alarm = self.seconds_till_alarm(dawn)
        print 'Seconds till dawn: ', seconds_to_alarm
        self._log('Seconds till dawn: ' + str(seconds_to_alarm))

        self.dawn_timer = threading.Timer(seconds_to_alarm, self.trigger_dawn)
        self.dawn_timer.start()
        # self.threads['dawn'] = dawn
        self.next_alarm = next_alarm

    # Setup dawn transition
    # Create a thread for sunrise
    def trigger_dawn(self):
        self._log('trigger_dawn()')
        print 'trigger_dawn'

        duration = self.next_alarm['dawn']['duration']
        self.lights.dawn(duration)

        sunrise = self.next_alarm['sunrise']['end_time'] - self.next_alarm['sunrise']['duration']
        seconds_to_sunrise = self.seconds_till_alarm(sunrise)
        print 'Seconds till sunrise: ', seconds_to_sunrise
        self.sunrise_timer = threading.Timer(seconds_to_sunrise, self.trigger_sunrise)
        self.sunrise_timer.start()

    # Setup sunrise transition
    # Create a thread for day
    def trigger_sunrise(self):
        self._log('trigger_sunrise()')
        print 'trigger_sunrise'

        duration = self.next_alarm['sunrise']['duration']

        self.lights.sunrise(duration)

        # Setup auto-shutoff
        day_ends = self.next_alarm['day']['end_time']
        seconds_of_day = self.seconds_till_alarm(day_ends)
        print 'seconds_of_day', seconds_of_day
        self.shutoff_thread = threading.Timer(seconds_of_day, self.trigger_autoshutoff)
        self.shutoff_thread.start()

    # Execute day routine (shut lights off)
    def trigger_autoshutoff(self):
        self._log('trigger_autoshutoff()')
        print 'turning lights off'

        self.lights.shutoff(self.SHUTOFF_DURATION)

        # Set tomorrow's alarm
        self.set_alarm()

    # Returns the number of seconds until an event
    def seconds_till_alarm(self, end_time, start_time=False):
        self._log('seconds_till_alarm()', end_time)
        if not start_time:
            start_time = datetime.datetime.now()

        countdown_to_alarm = end_time - start_time
        return countdown_to_alarm.total_seconds()

    # Returns alarm for day of the week
    # 0 is Sunday
    # 1 Monday
    # 2 Tuesday
    # 3 Wednesday
    # 4 Thursday
    # 5 Friday
    # 6 Saturday
    def get_alarm_for_day_number(self, day_number):
        self._log('get_alarm_for_day_number()', day_number)
        day_number = int(day_number)
        if day_number > 6:
            day_number = 0
        now = datetime.datetime.now()
        today_number = int(now.strftime("%w"))

        alarm = self.settings.get_alarm_for_day(day_number)

        hour = alarm['hour']
        minutes = alarm['minutes']

        alarm_day = now
        # Calculate date based on difference between day numbers
        increment = datetime.timedelta(days=1)
        # Keep adding days until the alarm day number is the same as the parameter day number
        while int(alarm_day.strftime("%w")) is not day_number:
            alarm_day += increment

        dawn_duration = datetime.timedelta(minutes=15)
        sunrise_duration = datetime.timedelta(minutes=15)
        auto_shutoff_delay = datetime.timedelta(hours=2)

        year = alarm_day.strftime("%Y")
        month = alarm_day.strftime("%m")
        day = alarm_day.strftime("%d")

        sunrise_end = datetime.datetime(int(year), int(month), int(day), int(hour), int(minutes))
        dawn_end = sunrise_end - sunrise_duration
        day_ends = sunrise_end + auto_shutoff_delay

        dawn = {'end_time': dawn_end, 'duration': dawn_duration}
        sunrise = {'end_time': sunrise_end, 'duration': sunrise_duration}
        day = {'end_time': day_ends}

        return {'dawn': dawn, 'sunrise': sunrise, 'day': day}

    def get_today_alarm(self):
        self._log('get_today_alarm()')
        now = datetime.datetime.now()
        day_number = now.strftime("%w")

        today_alarm = self.get_alarm_for_day_number(day_number)

        return today_alarm

    # Gets next alarm (typically tomorrow's)
    def get_next_alarm(self):
        self._log('get_next_alarm()')
        now = datetime.datetime.now()
        today_alarm = self.get_today_alarm()

        if now >= today_alarm['sunrise']['end_time']:
            self._log('get_next_alarm', 'get tomorrow')
            print "now >= today_alarm['sunrise']['end_time'])"
            day_number = int(now.strftime("%w"))
            next_alarm = self.get_alarm_for_day_number(day_number + 1)
        else:
            self._log('get_next_alarm', 'get today alarm')
            print now, today_alarm['sunrise']['end_time']
            next_alarm = today_alarm

            # Demo mode ######################
            # dawn_duration = datetime.timedelta(minutes=1)
            # sunrise_duration = datetime.timedelta(minutes=1)
            # auto_shutoff_delay = datetime.timedelta(minutes=1)
            #
            # sunrise_delay = dawn_duration + sunrise_duration + datetime.timedelta(seconds=5)
            #
            # sunrise_end = datetime.datetime.now() + sunrise_delay
            # dawn_end = sunrise_end - sunrise_duration
            # day_ends = sunrise_end + auto_shutoff_delay
            #
            # dawn = {'end_time': dawn_end, 'duration': dawn_duration}
            # sunrise = {'end_time': sunrise_end, 'duration': sunrise_duration}
            # day = {'end_time': day_ends}
            # return {'dawn': dawn, 'sunrise': sunrise, 'day': day}

        # END DEMO MODE ##################

        return next_alarm

    # Cleans up all running threads
    def shutdown(self):
        self.lights.lights_off()
        self.keep_running = False
        self.dawn_timer.cancel()
        self.sunrise_timer.cancel()
        self.shutoff_thread.cancel()
        self.rabbit_listener_thread.join()
        # self.lights.shutdown()

    def _log(self, method_name, message=None):
        log_line = str(method_name)

        if message:
            log_line += ': ' + str(message)

        self.logger.write(log_line, 'Aurora')