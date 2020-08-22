from flask import Flask, render_template, jsonify, request
from selenium import webdriver
from datetime import date, timedelta
import pyautogui
import time
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhomework

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

driver.get('https://mycompany.hyundaicard.com')

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.moveTo(1173,350,1)
pyautogui.doubleClick(x=1173,y=350, button='left')

#현대카드 홈페이지 내에 메뉴 화면 없애기
pyautogui.moveTo(33,844,1)
pyautogui.click(x=33,y=844,button='left')
#아이디 화면 띄우기
pyautogui.moveTo(153,564,1)
pyautogui.doubleClick(x=153,y=564, button='left')

driver.find_element_by_id("corp_web_mbr_id").send_keys('kuksan88')

time.sleep(10)

# My account
pyautogui.click(x=478,y=230, button='left', duration=1)
# 카드이용 내역
pyautogui.click(x=481,y=385, button='left', duration=1)

# 직접입력
pyautogui.click(x=1190,y=645, button='left', duration=1)

today = date.today()
first_day = today.replace(day=1)

last_day_month_ago = first_day - timedelta(days=1)

first_day_month_ago = last_day_month_ago.replace(day=1)

time.sleep(1)
driver.find_element_by_id("strtDt").click()
time.sleep(1)
driver.find_element_by_id("endDt").send_keys(print(first_day_month_ago))

time.sleep(1)
driver.find_element_by_id("endDt").click()
time.sleep(1)
driver.find_element_by_id("endDt").send_keys(print(last_day_month_ago))

# 확인 버튼
driver.find_element_by_xpath("//div[@class='medium_btn_type_02']").click()


# 월초 달력 화면
#pyautogui.click(x=686,y=585, button='left', duration=1)
# 달력 내 월초 클릭
#pyautogui.write("20200701", interval=0.5)

# 월말 달력 화면
#pyautogui.click(x=920,y=585, button='left', duration=1)