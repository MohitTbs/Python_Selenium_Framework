import time

import pytest

from Pages.home_page import HomePage
from Pages.product_page import ProductPage
from TestData.DataUtil import dp2
from Utilities.ConfigReader import read_configuration


class Test_Search:
    @pytest.mark.parametrize('product_name', dp2('test_search_product'))
    def test_search_product(self, product_name):
        self.driver.get(read_configuration('urls', "mainUrl"))
        homePage = HomePage(self.driver)
        homePage.click_on_product_link()
        productPage = ProductPage(self.driver)
        productPage.enter_product_name(product_name)
        productPage.click_on_submit_search_btn()
        l1 = productPage.get_name_of_all_products()
        f1 = True
        for i in l1:
            if product_name in i.lower():
                print(i)
                f1 = False
                assert True
                break
        if f1:
            assert False
