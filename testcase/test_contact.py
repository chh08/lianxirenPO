from page.base_page import BasePage
from page.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainpage = MainPage()

    def test_addmember(self):
        username = 'xiaoming'
        account = '666'
        phonenum = '13112345678'
        page = self.mainpage.goto_add_member()
        page.add_member(username, account, phonenum)
        names = page.get_member()
        # 断言
        assert username in names

    def test_maillist_addmember(self):
        username = 'xiaoming'
        account = '666'
        phonenum = '13112345678'
        page = self.mainpage.goto_maillist()
        page.add_member(username, account, phonenum)
        names = page.get_member()
        # 断言
        assert username in names
