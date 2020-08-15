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
#현대카드 횸페이지 내리기
pyautogui.moveTo(1779,19,3)
pyautogui.click(x=1779,y=19)
#아이디 화면 띄우기
pyautogui.moveTo(138,71,3)
pyautogui.doubleClick(x=138,y=71, button='left')
#아이디 글씨 클릭 후 드래그
pyautogui.moveTo(593,336,3)
pyautogui.dragTo(682,332,1,button='left')
#아이디 글씨 드래그 후 복사
pyautogui.moveTo(645,335,1)
pyautogui.click(x=645,y=335,button='right')
#아이디 글씨 드래그 후 복사 버튼 클릭
pyautogui.moveTo(675,352,1)
pyautogui.click(x=675,y=352,button='left')
#현대카드 홈페이지 띄우기
pyautogui.moveTo(1350,16,1)
pyautogui.click(x=1350,y=16,button='left')

#현대카드 홈페이지 내에 메뉴 화면 없애기
pyautogui.moveTo(33,844,3)
pyautogui.click(x=33,y=844,button='left')
#아이디 화면
pyautogui.moveTo(182,540,1)
pyautogui.click(x=182,y=540,button='left')
#아이디 복사 붙여넣기 메뉴
pyautogui.moveTo(181,540,1)
pyautogui.click(x=181,y=540,button='right')
#아이디 복사 붙여넣기 하기
pyautogui.moveTo(279,746,1)
pyautogui.click(x=279,y=746,button='left')
