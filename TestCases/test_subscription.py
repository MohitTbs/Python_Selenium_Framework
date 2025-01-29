import pytest

from Pages.home_page import HomePage
from TestData.DataUtil import dp2
from Utilities.ConfigReader import read_configuration


class Test_Subscription:
    @pytest.mark.parametrize('random_email', dp2('test_email_is_subscribed'))
    def test_email_is_subscribed(self, random_email):
        self.driver.get(read_configuration('urls', "mainUrl"))
        homePage = HomePage(self.driver)
        homePage.enter_email_in_subscription_box(random_email)
        homePage.click_on_subscribe_btn()
        assert homePage.get_subscription_success_msg()
