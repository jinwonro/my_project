from flask import Flask, render_template, jsonify, request
from datetime import date, timedelta
import requests
import pyautogui
import time

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework

today = date.today()
first_day = today.replace(day=1)

last_day_month_ago = first_day - timedelta(days=1)

first_day_month_ago = last_day_month_ago.replace(day=1)

print(last_day_month_ago)



