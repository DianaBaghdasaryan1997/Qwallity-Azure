from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
from Helper.general_helper import GeneralHelper


class EntryQwallityPage(GeneralHelper):
    inp_email = (By.ID, "email")
    inp_code= (By.ID, "code")
    btn_send = (By.ID, "Send")

    def enter_to_qwallity_app(self, email, code): 

        self.find_elem_and_send_data(self.inp_email, email)
        self.find_elem_and_send_data(self.inp_code, code)
        self.find_and_click_elem(self.btn_send)


