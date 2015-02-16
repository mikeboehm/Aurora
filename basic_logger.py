from datetime import datetime
import os


class Logger(object):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    log_filename = '/logs/all_events.log'

    def __init__(self):
        print self.__location__
        print self.__location__
        print self.__location__
        print self.__location__

    def write(self, log_record, class_name=None):
        log_file = self.__location__ + self.log_filename

        all_events = open(log_file, 'a')
        now = datetime.now()

        if class_name:
            log_record = class_name + ': ' + log_record

        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        line_to_write = formatted_date + ' - ' + log_record + "\n"

        all_events.write(line_to_write)

        all_events.close()