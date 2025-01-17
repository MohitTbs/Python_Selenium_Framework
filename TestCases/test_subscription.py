from Pages.home_page import HomePage
from Utilities.ConfigReader import read_configuration


class Test_Subscription:

    def test_email_is_subscribed(self):
        self.driver.get(read_configuration('urls', "mainUrl"))
        homePage = HomePage(self.driver)
        homePage.enter_email_in_subscription_box("gsjdgsah@hj.cj")
        homePage.click_on_subscribe_btn()
        assert homePage.get_subscription_success_msg()
