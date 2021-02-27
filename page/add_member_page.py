
from selenium.webdriver.remote.webdriver import WebDriver

from page.base_page import BasePage


class AddMemberPage:
    """添加成员类"""
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self, username, account, phonenum):
        """添加联系人"""
        # 输入 用户名
        username = 'xiaoming'
        account = '666'
        phonenum = '13112345678'
        # 输入用户名
        self.driver.find_element_by_id('username').send_keys(username)
        # 输入账号
        self.driver.find_element_by_id('memberAdd_acctid').send_keys(account)
        # 输入手机号
        self.driver.find_element_by_id('memberAdd_phone').send_keys(phonenum)
        # 点击保存,页面上有多个相同属性元素时，通过find_element找到的时第一个元素
        self.driver.find_element_by_css_selector('.js_btn_save').click()

        return True

    def get_member(self):
        """获取所有的联系人姓名"""
        eles_list = self.driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute('title'))

        return names
