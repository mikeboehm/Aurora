from unittest import TestCase
from basic_logger import Logger

__author__ = 'mike'


class TestLogger(TestCase):
    def test_get_log_file_path(self):
        logger = Logger('class_name', 'log_file.log', 'log_path')

        print logger.get_log_file_path()

    def test_log(self):
        pass
        # self.fail()

    def test_write(self):
        pass
        # self.fail()