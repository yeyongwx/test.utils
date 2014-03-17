#-*-coding:utf-8-*-


'''
加上 chromedriver.exe 和 IEDriverServer.exe 后，降代码的第六行改成
driver = webdriver.Ie()   或    driver = webdriver.Chrome() 可测试在IE或Chrome下的效果。
'''



from selenium import webdriver
import unittest
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #driver = webdriver.Ie()
        #driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://blog.csdn.net"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/spring292713")
        driver.find_element_by_link_text(u"登录").click()
        driver.switch_to_frame("logfrm")
        driver.find_element_by_id("u").clear()
        driver.find_element_by_id("u").send_keys("spring292713")
        driver.find_element_by_id("p").clear()
        driver.find_element_by_id("p").send_keys("xxxoo")
        driver.find_element_by_id("aLogin").click()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()