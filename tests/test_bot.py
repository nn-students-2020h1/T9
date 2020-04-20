# -*- coding: utf-8 -*-
import unittest
from io import StringIO
from unittest import mock
from unittest.mock import patch

from modules.sql import SqlDataBase

TEST_LOG_DATA = {
    "userId": '1',
    "userName": 'bot',
    "call": 'func1',
    "message": 'test message',
    "time": '2020-04-20 22:33:37'
}


class TestsLogs(unittest.TestCase):
    def setUp(self) -> None:
        self.dataBase = SqlDataBase("test.db", check_thread=False)
        if 'log' not in self.dataBase.tables:
            fields = '''
            userId integer,
            userName text,
            call text,
            message text,
            time text
            '''
            self.dataBase.createTable('log', fields)

    def test_log_save(self):
        self.dataBase.addRecord("log", TEST_LOG_DATA)
        log = self.dataBase.getRecords(
            'log', "SELECT userName, message FROM log WHERE userId=1 ORDER BY time DESC", 1)
        self.assertEqual(log, [("bot", "test message")])
