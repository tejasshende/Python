from selenium import webdriver

class page(object):
    
    # def __init__(self,driver):
    #     self.driver=driver
    
    def launchBrowser(self,driver,app_url):
        driver.get(app_url)
        driver.maximize_window
        
    def typeKeys(driver,locator,value):
        driver.find_element_by_xpath(locator).sendKeys(value)
        
    def clickElement(driver,locator):
        driver.find_element_by_xpath(locator).click()