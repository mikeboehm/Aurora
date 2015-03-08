from datetime import datetime
import os


class Logger(object):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    def __init__(self, class_name = None, filename='all_events.log', log_dir='logs'):
        self.class_name = class_name
        self.filename = filename
        self.log_dir = log_dir

    def get_log_file_path(self):
        return os.path.join(self.__location__, self.log_dir, self.filename)

    def log(self, method_name, message=None):
        log_line = str(method_name)

        if message:
            log_line += ': ' + str(message)

        self.write(log_line, self.class_name)

    def write(self, log_record, class_name=None):
        all_events = open(self.get_log_file_path(), 'a')
        now = datetime.now()

        if class_name:
            log_record = class_name + ': ' + log_record

        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        line_to_write = formatted_date + ' - ' + log_record + "\n"

        all_events.write(line_to_write)

        all_events.close()