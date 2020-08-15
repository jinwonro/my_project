from flask import Flask, render_template, jsonify, request
import pyautogui

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework

print("Current Mouse Position :", pyautogui.position())