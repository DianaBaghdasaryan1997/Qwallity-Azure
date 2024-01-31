from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os

class GeneralHelper():
    def __init__(self, driver):
        self.driver = driver  

    def navigate_to_url(self, url):
        try:
            self.driver.get(url)
            self.driver.set_page_load_timeout(20)
            logging.info(f"Navigated to URL: '{url}'")
            return self.driver

        except Exception as e:
            logging.error(f"Error navigating to URL: '{url}'. {e}")
            raise
        
    def open_new_tab(self, driver, url):
        try:
            driver.execute_script("window.open();")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
            logging.info(f"Opened a new tab with URL: {url}")
        except Exception as e:
            logging.error(f"Error opening a new tab: {e}")
            raise
            
             
    #Work with web elements.
    def find_elem_in_ui(self, locator, timeout=120):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)  
                )                                                                             
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logging.info(f"Element {locator} found and is now visible.")
            return element
        
        except Exception as e:
            logging.error(f"Error finding element {locator} or waiting for visibility: {e}")
        
    def find_elem_in_dom(self, locator, timeout=120):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator) 
            )
            logging.info(f"Element {locator} found and is now present.")
            return element
        except Exception as e:
            logging.error(f"Error finding element {locator} or waiting for presence: {e}")
            raise
        
    def find_and_click_elem(self, locator, timeout=120):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)
            )
            element.click()
            logging.info(f"Clicked on element {locator}.")
            return element
    
        except Exception as e:
            logging.error(f"Error finding element {locator} or clicking: {e}")
            raise
        
    def find_elem_and_send_data(self, locator, input_data, timeout=120):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.send_keys(input_data)
            logging.info(f"Sent keys '{input_data}' to element {locator}.")
            return element
    
        except Exception as e:
            logging.error(f"Error finding element {locator} or sending keys: {e}")
            raise
             
    def delete_file(self, file_name):
        try:
            file_path = os.path.join(os.path.dirname(__file__), file_name)

            if os.path.exists(file_path):
                confirm = input(f"Do you want to remove '{file_name}' file? (yes/no): ")

                if confirm.lower() == "yes":
                    os.remove(file_path)
                    print(f"'{file_name}' file has been deleted.")
                elif confirm.lower() == "no":
                    print(f"'{file_name}' file hasn't been deleted.")
                else:
                    print(f"'{file_name}' file hasn't been deleted, because of incorrect input.")
            else:
                print(f"'{file_name}' file doesn't exist.")

        except Exception as e:
            print(f"Error occurred while deleting '{file_name}' file. Exception: {e}")
       

    
        
    

        
    