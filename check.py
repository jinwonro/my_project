from flask import Flask, render_template, jsonify, request
import pyautogui

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework

#현대카드 홈페이지
pyautogui.moveTo(51,58,2)
pyautogui.doubleClick(x=51,y=58, button='left')
#현대카드 아이디
pyautogui.moveTo(233,485,3)
pyautogui.click(x=233,y=485)
#현대카드 아이디
pyautogui.moveTo(190,553,3)
pyautogui.click(x=190,y=553)


#현대카드 아이디 화면
pyautogui.moveTo(163,542,1)
pyautogui.click(x=163,y=542,button='left')


#패스워드 화면 띄우기
pyautogui.moveTo(1513,23,1)
pyautogui.click(x=1513,y=23,button='left')

pyautogui.moveTo(590,389,1)
pyautogui.click(x=590,y=389,button='left')

pyautogui.moveTo(593,390,1)
pyautogui.dragTo(706,386,1,button='left')

pyautogui.moveTo(646,387,1)
pyautogui.click(x=646,y=387,button='right')

pyautogui.moveTo(739,404,1)
pyautogui.click(x=739,y=404,button='left')

pyautogui.moveTo(739,404,1)
pyautogui.click(x=739,y=404,button='left')

pyautogui.moveTo(1328,24,1)
pyautogui.click(x=1328,y=24,button='left')

pyautogui.moveTo(16,582,3)
pyautogui.moveTo(167,589,1)
pyautogui.click(x=167,y=589,button='left')

pyautogui.moveTo(168,589,1)
pyautogui.click(x=168,y=589,button='left')