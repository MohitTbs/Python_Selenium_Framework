import time
from Utilities.ConfigReader import read_configuration


class Test_Demo1:

    def test_dem1(self):
        self.driver.get(read_configuration('urls', "mainUrl"))
        time.sleep(2)
