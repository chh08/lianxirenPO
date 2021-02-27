from time import sleep

from page.add_member_page import AddMemberPage
from page.base_page import BasePage


class MainPage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_add_member(self):
        """添加成员"""
        # 点击添加成员,使用nth-child定位
        self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(1)').click()
        # 跳转添加页面
        return AddMemberPage(self.driver)

    def goto_maillist(self):
        """通讯录页面添加成员"""
        # 点击通讯录
        self.driver.find_element_by_id('menu_contacts').click()
        # 点击添加成员,页面上有多个相同属性元素时，通过find_element找到的时第一个元素
        sleep(2)
        self.driver.find_element_by_link_text('添加成员').click()
        # 跳转添加页面
        return AddMemberPage(self.driver)
