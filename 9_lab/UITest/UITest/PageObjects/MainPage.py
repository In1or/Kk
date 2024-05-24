from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PageObjects.BasePage import BasePage
from tests.conf import *
from selenium import webdriver
import time

class MainPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)      
        self._PRODUCT_CLASS = 'product-main'
        self._BTN_ADD_TO_CART = 'ADD TO CART'
        self._BTN_CLOSE_CLASS = 'close'
        self._BTN_PRIMARY_CLASS = 'btn-primary'
        
        self._TEST_PRODUCT_NAME = 's'
        self._TEST_PRODUCT_VALUE = 'часы9'
        
        self._FIRST_PRODUCT = '1234'
        self._PRODUCTS_NAME_XPATH = "//*[@id='cart']/div/div//a"
        self._SECOND_PRODUCT = 'CASIO GA-1000-1AER'
        
        self._LOGO_XPATH = '/html/body/div[2]/a'
        self._CATEGORY_NAME_XPATH = '/html/body/div[4]/div[2]/div/div/ol/li[2]/a'
        
    def click_on_hyperlink(self, hyperlink_text):
        elem = self._driver.find_element(By.LINK_TEXT, hyperlink_text)
        elem.click()
        time.sleep(1)
        
    def find_elem_by_xpath(self, xpath):
        elem = self._driver.find_element(By.XPATH, xpath)
        return elem       

    def find_elems_by_xpath(self, xpath):
        elems = self._driver.find_elements(By.XPATH, xpath)
        return elems


    def enter_value_in_input_with_enter(self, input_name, value):
        elem = self._driver.find_element(By.NAME, input_name)
        elem.send_keys(value)
        elem.send_keys(Keys.RETURN)

    def click_on_button(self, button_class_name):
        elem = self._driver.find_element(By.CLASS_NAME, button_class_name)
        elem.click()
        
    def check_availaility(self, elem_class_name):
        try:
            elem = self._driver.find_element(By.CLASS_NAME, elem_class_name)
            return True
        except:
            return False
        
    def close(self):
        self._driver.close()      

    def go_back(self):
        self._driver.execute_script("window.history.go(-1)")        
