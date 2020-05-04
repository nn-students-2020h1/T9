# -*- coding: utf-8 -*-
import os

import pymongo

TOKEN = os.environ.get("TOKEN")  # insert your token here
PROXY = 'https://telegg.ru/orig/bot'  # proxy to connect against telegram ban

# Initialize MongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client.T9_bot
