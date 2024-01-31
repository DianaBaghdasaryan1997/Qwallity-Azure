from datetime import datetime
import logging

logging.info(f"Program has started at: {datetime.now()}")

def test_assert_1():
    assert 100 == 100
    
def test_assert_2():
    assert 150 == 150
    
def test_assert_3():
    assert 200 == 200
    
logging.info(f"Program has ended at: {datetime.now()}")