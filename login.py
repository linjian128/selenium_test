# -*- coding: utf-8 -*
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.get("http://sso.iot.test.lngtop.com/")

try:
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "loginName")))
finally:
    #browser.close()
    pass

assert browser.current_url == "http://passport.test.lngtop.com/#/login?appKey=c2ad90d8a1e440acac18477160d8ec4b&appType=web&returnUrl=http:%2F%2Fsso.iot.test.lngtop.com%2Findex.html%23%2Fmain"

browser.find_element_by_name("loginName").send_keys("15160138958")
browser.find_element_by_name("password").send_keys("admin123")
browser.find_element_by_xpath("//button[@w5c-form-submit='login()']").click()

try:
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//label[contains(.,'新版')]")))
finally:
   # browser.close()
   pass

assert browser.title == u"云顶物联网平台"

browser.find_element_by_xpath("//label[contains(.,'新版')]").click()
assert 'No results found.' not in browser.page_source 

# 点击 用户名 
sleep(2)
browser.find_element_by_xpath("//a[@aria-haspopup='true']").click()
# 点击个人信息
sleep(2)
browser.find_element_by_xpath("//a[@href='#/personalData']").click()

sleep(2)
browser.find_element_by_xpath("//span[contains(.,'气化站运营')]").click()
sleep(2)
browser.find_element_by_xpath("//span[contains(.,'储罐监控')]").click()
