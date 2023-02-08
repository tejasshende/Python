import sys
sys.path.append('src/test/page_objects')
from selenium import webdriver
from page import page

class googlePage():

    #locators
    searchBox = "//input[@name='q']"
    searchButton = "(//input[@value='Google Search'])[2]"

    def __init__(self,driver):
        self.driver = driver
        
    def verifyTitle(self,title_to_be_verified):
        # p = page(self.driver)
        page.launchBrowser(self.driver,"www.google.com")
        if self.driver.title == title_to_be_verified:
            assert True
        else:
            assert False
            
    def searchKeyword(self,driver,keyword):
        page.typeKeys(self.searchBox,keyword)
        