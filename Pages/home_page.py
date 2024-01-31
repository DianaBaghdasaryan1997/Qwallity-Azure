from selenium.webdriver.common.by import By
from Helper.general_helper import GeneralHelper

class HomePage(GeneralHelper):
    
    btn_register_home = (By.XPATH, "//a[text()='Register']")
    btn_login_home = (By.XPATH, "//a[text()='Login']")
    btn_logout_home = (By.XPATH, "//a[text()='Logout']")
    
    def click_register_button(self):
        self.find_and_click_elem(self.btn_register_home)
        
    def click_login_button(self):
        self.find_and_click_elem(self.btn_login_home)
        
    def click_login_button(self):
        self.find_and_click_elem(self.btn_logout_home)
        
    
    
    



    
