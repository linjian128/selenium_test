# -*- coding: utf-8 -*
import unittest
from selenium import webdriver
from time import sleep



class TestLogin(unittest.TestCase):
    def test_login(self):
        # Login
        self.assertEqual(browser.current_url,'http://passport.test.lngtop.com/#/login?appKey=c2ad90d8a1e440acac18477160d8ec4b&appType=web&returnUrl=http:%2F%2Fsso.iot.test.lngtop.com%2Findex.html%23%2Fmain')
        browser.find_element_by_name("loginName").send_keys("15160138958")
        browser.find_element_by_name("password").send_keys("admin123")
        browser.find_element_by_xpath("//button[@w5c-form-submit='login()']").click()
        sleep(3)
        self.assertEqual(browser.title,u'云顶物联网平台')

if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get("http://sso.iot.test.lngtop.com/")
    sleep(5)
    unittest.main()
