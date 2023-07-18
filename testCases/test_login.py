import pytest
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen

class Test001Login:
    baseURL = "https://login.salesforce.com/"
    username = "vinod.bendre@axtria.com.int"
    password = "@xtria@123"
    logger = LogGen.loggen()

    def test_homepage_title(self, setup):
        self.logger.info("**************************Test_001_Login**********************")
        self.logger.info("**************************Homepage Verify Title**********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Login | Salesforce":
            assert True
        else:
            self.driver.save_screenshot("test_homepageTitle.png")
            self.driver.close()
            self.logger.info("**************************Login Test Title verification return "
                             "false**********************")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Lightning Experience | Salesforce":
            assert True
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_loginTitle.png")
            self.driver.close()
            assert False
