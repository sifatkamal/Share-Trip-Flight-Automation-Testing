import os
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from openpyxl import load_workbook
from datetime import datetime
import time

class Booking:

    def __init__(self, driver_path = r"C:/SeleniumDrivers", teardown = False):

        self.driver_path = driver_path
        self.teardown = teardown

        os.environ['PATH'] += self.driver_path

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        if self.teardown == True:
            
            self.driver.quit()

    def land_page(self):

        self.driver.get(const.BASE_URL)

    def flight_search(self):

        # self.driver.find_element(By.XPATH, '(//label[@class="MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd mui-style-83snne"])[1]').click()

        self.driver.find_element(By.CSS_SELECTOR, 'button[id="traveller-count-button"]').click()

        # 2 adults

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[9]').click()

        # 1 child

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[11]').click()

        # 1 kids

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[13]').click()

        # 1 infants

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[15]').click()

        self.driver.find_element(By.TAG_NAME, "body").click()

        time.sleep(3)

        # Traveling type

        self.driver.find_element(By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation mui-style-1v7znae"]').click()

        time.sleep(6)

        self.driver.find_element(By.XPATH, '(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-1mmzlec"])[12]').click()

        self.driver.find_element(By.TAG_NAME, "body").click()


        # Student Fare

        self.driver.find_element(By.XPATH, '(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-1mmzlec"])[5]').click()

        round_trip_flight_info = self.driver.find_elements(By.XPATH, '//div[@class="MuiStack-root mui-style-1r5to7m"]')

        assert len(round_trip_flight_info) == 4


        # One Way

        self.driver.find_element(By.XPATH, '(//label[@class="MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd mui-style-83snne"])[1]').click()

        one_way_flight_info = self.driver.find_elements(By.XPATH, '//div[@class="MuiStack-root mui-style-1r5to7m"]')

        assert len(one_way_flight_info) == 3

        # Multi City

        self.driver.find_element(By.XPATH, '(//label[@class="MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd mui-style-83snne"])[2]').click()

        # Add more
        
        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[4]').click()

        flight_info = self.driver.find_elements(By.XPATH, '(//div[@class="MuiStack-root mui-style-1r5to7m"])')

        time.sleep(6)

        assert len(flight_info) == 9

        # Search button check

        search_check = self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[6]')

        assert search_check is not None

