from Helper.general_helper import GeneralHelper
from selenium.webdriver.common.by import By

class LoginPage(GeneralHelper):
    
    inp_username = (By.XPATH, "//input[@name='username']")
    inp_password = (By.XPATH, "//input[@name='password']")
    btn_login = (By.XPATH, "//button[text()='Log in']")
    
    def log_in(self, username, password):
        self.find_elem_and_send_data(self.inp_username, username)
        self.find_elem_and_send_data(self.inp_password, password)
        self.find_and_click_elem(self.btn_login)
        