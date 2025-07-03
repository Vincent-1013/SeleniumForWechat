from selenium_wework_main.page.main import Main


class TestAddMember:

    def setup_method(self):
        self.main = Main()



    def test_add_member(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        assert "Wei001" in add_member.get_member()


