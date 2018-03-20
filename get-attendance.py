from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import os

options = webdriver.ChromeOptions()
options.add_argument("headless")

# your executable path is wherever you saved the chrome webdriver
chromedriver = "C:\\Users\\rajsi\\Downloads\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver,chrome_options = options)
print("opening niet page")
browser.get("http://www.nietcampus.com/Home/")
email = browser.find_element_by_id("txtUserName")
email.send_keys("0161mec121")
pwd = browser.find_element_by_id("txtPassword")
pwd.send_keys("password")
submission = browser.find_element_by_name("Ulogin")
print("inputing credentials and opening main login page")
submission.click()
browser.get("http://www.nietcampus.com/manage/AttendanceReport/SubjectCodeWiseSemAttendence.aspx")
time.sleep(1)
select1= Select(browser.find_element_by_id("ctl00_ctl00_ContentPane_ContentPane_AttendenceColor_ddlSession"))
select1.select_by_value("Sess000011")
print("selecting entries......")
time.sleep(3)
select2=Select(browser.find_element_by_id("ctl00_ctl00_ContentPane_ContentPane_AttendenceColor_DDLInstitute"))
select2.select_by_value("IM00000001")
time.sleep(3)
select3=Select(browser.find_element_by_id("ctl00_ctl00_ContentPane_ContentPane_AttendenceColor_ddlprogram"))
select3.select_by_value("PG00000001")
time.sleep(3)
select4=Select(browser.find_element_by_id("ctl00_ctl00_ContentPane_ContentPane_AttendenceColor_ddlbranch"))
select4.select_by_value("BR04")
time.sleep(2)
select5=Select(browser.find_element_by_id("ctl00_ctl00_ContentPane_ContentPane_AttendenceColor_ddlsem"))
select5.select_by_value("CS04")
print("done")
time.sleep(1)
view=browser.find_element_by_id("ctl00_ctl00_ContentPane_ContentPane_AttendenceColor_btnView")
print("waiting for attendance table to load")
view.click()
time.sleep(10)

soup = BeautifulSoup(browser.page_source, "html.parser")

tabledata = soup.find(id="ctl00xctl00xContentPanexContentPanexAttendenceColorxUltraWebGrid1_r_122")  #edit this to get your attendance
rows = tabledata.findChildren('td')
n=0
for row in rows:
    n= n+1
    if(n==19):
        print("YOur attendance is:  ",row.getText())

browser.quit()    
