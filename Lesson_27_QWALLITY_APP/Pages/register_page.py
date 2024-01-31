from selenium.webdriver.common.by import By
from Helper.general_helper import GeneralHelper
from Pages.home_page import HomePage

class RegisterPage(GeneralHelper):
    
    

    inp_name = (By.XPATH, "//input[@id='name']")
    inp_email = (By.XPATH, "//input[@id='email']")
    inp_username = (By.XPATH, "//input[@id='username']")
    inp_password = (By.XPATH, "//input[@id='password']")
    inp_confirm_password = (By.XPATH, "//input[@id='confirm']")
    btn_submit = (By.XPATH, "//input[@value='Submit']")

    def register_user(self, name, email, username, password):
  
        self.find_elem_and_send_data(self.inp_name, name)
        self.find_elem_and_send_data(self.inp_email, email)
        self.find_elem_and_send_data(self.inp_username, username)
        self.find_elem_and_send_data(self.inp_password, password)
        self.find_elem_and_send_data(self.inp_confirm_password, password)
        self.find_and_click_elem(self.btn_submit)
  
        return username, password
