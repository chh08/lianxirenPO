from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """基类"""
    base_url = ''

    def __init__(self, driver: WebDriver = None):
        # 初始化
        if driver == None:
            # 如果driver为空，进行初始化driver
            # 复用浏览器
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            # 设置隐式等待
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self.base_url != '':
            self.driver.get(self.base_url)