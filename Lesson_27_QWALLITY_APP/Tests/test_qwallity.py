import sys
from datetime import datetime
from Helper.general_helper import GeneralHelper
from Pages.qwallity_entry_page import EntryQwallityPage
from Pages.home_page import HomePage
from Pages.register_page import RegisterPage
from Pages.login_page import LoginPage
from Test_Data.test_data import credentials
from config import *
import logging


def test_qwallity_app(driver):
    logging.info(f"Program has started at: {datetime.now()}")
    
    qwallity_entry_obj = EntryQwallityPage(driver) 
    qwallity_entry_obj.navigate_to_url(qwallity_url)
    qwallity_entry_obj.enter_to_qwallity_app(email_data, code_data)
    
    home_page_obj = HomePage(driver)
    home_page_obj.click_register_button()
    
    register_page_obj = RegisterPage(driver)
    username, password = register_page_obj.register_user(credentials["name"], credentials["email"], credentials["username"], 
                                    credentials["password"])
    login_page_obj = LoginPage(driver)
    login_page_obj.log_in(username, password)
    
    logging.info(f"Program has ended at: {datetime.now()}")