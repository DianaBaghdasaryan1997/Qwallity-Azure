from selenium import webdriver
import pytest
import logging
import pytest


@pytest.fixture()
def driver():
    try:
        # Run Chrome in headless mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        # driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    except Exception as error:
        raise Exception(error)


def pytest_configure():
    logging.basicConfig(filename= "my_log.log",
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S'
                        )