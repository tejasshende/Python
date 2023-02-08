import sys
sys.path.append('src/test')
import pytest
from selenium import webdriver
from page_objects.googlePage import googlePage 


class Test_Regression:       
        
    def test_Google(self,setup):
        self.driver = setup
        self.google = googlePage(self.driver)
        self.google.verifyTitle("Google")
        self.google.searchKeyword(self.driver,"selenium")
        

