from datetime import datetime


class Logger(object):
    log_filename = 'all_events.log'

    def write(self, log_record, class_name=None):
        all_events = open(self.log_filename, 'a')
        now = datetime.now()

        if class_name:
            log_record = class_name + ': ' + log_record

        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        line_to_write = formatted_date + ' - ' + log_record + "\n"

        all_events.write(line_to_write)

        all_events.close()