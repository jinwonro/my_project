import requests
from bs4 import BeautifulSoup
import openpyxl
import xlsxwriter

#path2 = "C:/test/paste.xlsx"

wb1 = openpyxl.Workbook()
ws1 = wb1.active

for page in range(10):
    raw = requests.get('http://consensus.hankyung.com/apps.analysis/analysis.list?&sdate=2018-07-01&edate=2019-07-31&report_type=CO&order_type=&now_page=' + str(page+1), headers={'User-Agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(raw, 'html.parser')
    reports = soup.select('#contents > div.table_style01 > table > tbody > tr')

    for report in reports:
        time = report.select_one('td.first.txt_number').text.strip()
        title = report.select_one('td.text_l > a').text.strip()
        opinion = report.select_one('td:nth-child(4)').text.strip()

#        ws1.append([time, title, opinion])
        print([time, title, opinion])

### wb1.save('test.xlsx', engine='xlsxwriter')