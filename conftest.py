import logging
import os

def pytest_configure():
    logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename=os.path.join(os.path.dirname(__file__), "my_logs.log"),
                    filemode='a',
                    encoding='utf-8'
                    )