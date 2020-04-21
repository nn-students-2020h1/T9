# -*- coding: utf-8 -*-
import unittest

import bot.log
from modules.sql import SqlDataBase

TEST_LOG_DATA = {
    "userId": '1',
    "userName": 'bot',
    "call": 'func1',
    "message": 'test message',
    "time": '2020-04-20 22:33:37'
}


@bot.log.log
def simple_action(update):
    return None


class TestLogs(unittest.TestCase):
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

        bot.log.dataBase = self.dataBase
        self.dataBase.delete_all_records("log")

    def tearDown(self):
        self.dataBase.delete_all_records("log")

    def test_log(self):
        update = {
            "_effective_user": {'id': 1, 'username': 'admin'},
            "message": {'text': "hello"}
        }
        simple_action(update)
        log = self.dataBase.getRecords(
            'log', "SELECT userName, message FROM log WHERE userId=1 ORDER BY time DESC", 1)
        self.assertEqual(log, [("admin", "hello")])

    def test_log_save(self):
        self.dataBase.addRecord("log", TEST_LOG_DATA)
        log = self.dataBase.getRecords(
            'log', "SELECT userName, message FROM log WHERE userId=1 ORDER BY time ASC", 1)
        self.assertEqual(log, [("bot", "test message")])
