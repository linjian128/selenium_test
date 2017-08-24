#!/usr/bin/python3.5
# -*- coding: utf-8 -*
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

import configparser
import codecs

cp = configparser.SafeConfigParser()
with codecs.open('config.conf', 'r', encoding='utf-8') as f:
    cp.readfp(f)

username = cp.get('user','username')
passwd = cp.get('user','passwd')

goods_name = cp.get('goods','name')
goods_s_add= cp.get('goods','s_add')
goods_price = cp.get('goods','price')


browser = webdriver.Firefox()
browser.get("http://operation.test.lngtop.com")


# -- login
#  username: linjian
#  password: linjian
browser.find_element_by_xpath("//input[@ng-model='user.loginid']").send_keys(username)
browser.find_element_by_xpath("//input[@ng-model='user.password']").send_keys(passwd)
browser.find_element_by_id("login-submit-btn").click()

#assert "电商后台管理系统" in browser.page_source
sleep(2)
assert browser.find_element_by_xpath("/html/body/div[1]/aside/div/nav/ul/li[3]")
print ("\033[1;31m Login Success! \033[0m")

sleep(2)
#--------------------------------------------------------------------------

#商品管理
# 新增商品
browser.find_element_by_xpath("/html/body/div[1]/aside/div/nav/ul/li[3]").click()
sleep(2)
browser.find_element_by_xpath("//span[contains(.,'商品信息')]").click()
sleep(2)
browser.find_element_by_xpath("//a[contains(.,'新增商品')]").click()
sleep(1)
browser.find_element_by_name("goodsName").send_keys(goods_name)
Select(browser.find_element_by_name('goodsInfo')).select_by_value(goods_s_add)
browser.find_element_by_name("v").send_keys(goods_price)
browser.find_element_by_xpath("//button[contains(.,'新增')]").click()

sleep(2)
assert goods_name in browser.find_element_by_xpath(" /html/body/div[1]/section/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div").text
sleep(1)
#--------------------------------------------------------------------------




'''
# 贸易采购
browser.find_element_by_xpath("/html/body/div[1]/aside/div/nav/ul/li[1]").click()
sleep(2)
browser.find_element_by_xpath("//span[contains(.,'供应商管理')]").click()
#browser.find_element_by_xpath("/html/body/div[1]/section/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[7]/button").click()
print (browser.find_element_by_xpath("/html/body/div[1]/section/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[7]/button").text)
print (browser.find_element_by_xpath("/html/body/div[1]/section/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div").text)

'''



'''
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
'''
