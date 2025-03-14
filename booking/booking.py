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

    def header(self):

        header_expected_hyperlink = ['Flight', 'Hotel', 'Shop', 'Holiday', 'Visa', 'Promotions', 'Business Class', 'Others', 'Login']

        visa_expected_options = ['Visa Application', 'Visa Guide', 'Transit Visa']

        others_options = ['About', 'SkyTrip', 'Why ShareTrip?', 'Travel Guide', 'News', 'FAQ & Support', 'Medical']

        count = 0

        hyperlink_1 = self.driver.find_elements(By.CSS_SELECTOR, 'span[class="MuiTypography-root MuiTypography-span mui-style-tdytol"]')

        hyperlink_2 = self.driver.find_elements(By.CSS_SELECTOR, 'p[class="MuiTypography-root MuiTypography-body1 mui-style-1aeqxg7"]')

        hyperlink_3 = self.driver.find_elements(By.CSS_SELECTOR, 'span[class="MuiTypography-root MuiTypography-span mui-style-h1xbi2"]')

        login = self.driver.find_elements(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[1]')

        hyperlink = hyperlink_1 + hyperlink_2 + hyperlink_3 + login

        for i in hyperlink:

            value = i.text

            if value in header_expected_hyperlink:

                count+=1    

        assert count == 9

        self.driver.find_element(By.XPATH, '(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-1aeqxg7"])[1]').click()

        listt = []

        for i in range(16, 19):

            option = self.driver.find_element(By.XPATH, '(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-1xhsunu"])[{}]'.format(i)).text

            listt.append(option)

        assert listt == visa_expected_options

        self.driver.find_element(By.TAG_NAME, "body").click()

        self.driver.find_element(By.XPATH, '(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-1aeqxg7"])[2]').click()

        listt = []

        for i in range(16, 23):

            option = self.driver.find_element(By.XPATH, '(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-1xhsunu"])[{}]'.format(i)).text

            listt.append(option)

        assert listt == others_options

    def flight_search(self):

        self.driver.find_element(By.CSS_SELECTOR, 'button[id="traveller-count-button"]').click()

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[9]').click()

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[11]').click()

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[13]').click()

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[15]').click()

        self.driver.find_element(By.TAG_NAME, "body").click()

        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation mui-style-1v7znae"]').click()

        time.sleep(6)

        self.driver.find_element(By.XPATH, '(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-1mmzlec"])[12]').click()

        self.driver.find_element(By.TAG_NAME, "body").click()

        self.driver.find_element(By.XPATH, '(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-1mmzlec"])[5]').click()

        round_trip_flight_info = self.driver.find_elements(By.XPATH, '//div[@class="MuiStack-root mui-style-1r5to7m"]')

        assert len(round_trip_flight_info) == 4

        self.driver.find_element(By.XPATH, '(//label[@class="MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd mui-style-83snne"])[1]').click()

        one_way_flight_info = self.driver.find_elements(By.XPATH, '//div[@class="MuiStack-root mui-style-1r5to7m"]')

        assert len(one_way_flight_info) == 3

        self.driver.find_element(By.XPATH, '(//label[@class="MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd mui-style-83snne"])[2]').click()
        
        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[4]').click()

        flight_info = self.driver.find_elements(By.XPATH, '(//div[@class="MuiStack-root mui-style-1r5to7m"])')

        time.sleep(6)

        assert len(flight_info) == 9

        search_check = self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[6]')

        assert search_check is not None

    






    def faq(self):

        expected_headline = 'Frequently Asked Questions'

        element = self.driver.find_element(By.XPATH, '(//h2[@class="MuiTypography-root MuiTypography-h2 mui-style-bxn3sk"])[6]')

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        textt = self.driver.find_element(By.XPATH, '(//h2[@class="MuiTypography-root MuiTypography-h2 mui-style-bxn3sk"])[6]').text

        assert textt == expected_headline

        element = self.driver.find_element(By.XPATH, '(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-12vri3f"])')

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        time.sleep(6)

        answer_list = []

        wait = WebDriverWait(self.driver, 10)

        for i in range(1, 7):

            question = wait.until(EC.element_to_be_clickable((By.XPATH, f'(//p[@class="MuiTypography-root MuiTypography-body1 mui-style-12vri3f"])[{i}]')))
            
            question.click()
            
            answer = self.driver.find_element(By.CSS_SELECTOR, 'div[class="MuiAccordionDetails-root mui-style-u7qq7e"]')

            answer_list.append(answer)

        assert len(answer_list) == 6

        self.driver.find_element(By.CSS_SELECTOR, 'div[class="MuiAccordionSummary-expandIconWrapper Mui-expanded mui-style-1fx8m19"]').click()

    
    
    
    def popular_airlines_and_flight_destination(self):

        headline = "Most Popular Airlines"

        element = self.driver.find_element(By.XPATH, '(//h2[@class="MuiTypography-root MuiTypography-h2 mui-style-bxn3sk"])[2]')

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        popular_airline_headline = element.text

        assert popular_airline_headline == headline

        element = self.driver.find_element(By.CSS_SELECTOR, 'a[class="mui-style-hx8sk2"]')

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        airlines = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="mui-style-hx8sk2"]')

        assert len(airlines) == 19

        time.sleep(3)



        headline = "Popular Flight Destinations from BD"

        element = self.driver.find_element(By.XPATH, '(//h2[@class="MuiTypography-root MuiTypography-h2 mui-style-bxn3sk"])[3]')

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        assert headline == element.text

        element = self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[4]')

        self.driver.execute_script("arguments[0].scrollIntoView();", element)


        box = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="MuiBox-root mui-style-lxguk4"]')

        listt_1 = []

        listt_2 = []

        for i in box:

            listt_1.append(i.text)

        time.sleep(6)
        

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[4]').click()

        box = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="MuiBox-root mui-style-lxguk4"]')

        for i in box:

            listt_2.append(i.text)

        assert listt_1 != listt_2

    def chepeast_flight_by_destination(self):

        element = self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[6]')

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        listt_1 = []

        listt_2 = []

        listt_3 = []

        destination = self.driver.find_elements(By.CSS_SELECTOR, 'p[class="MuiTypography-root MuiTypography-body1 hoverText mui-style-12xuhy5"]')

        for i in destination:

            value = i.text

            listt_1.append(value)

        assert len(listt_1) == 12

        time.sleep(6)

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[6]').click()

        destination = self.driver.find_elements(By.CSS_SELECTOR, 'p[class="MuiTypography-root MuiTypography-body1 hoverText mui-style-12xuhy5"]')

        for i in destination:

            value = i.text

            listt_2.append(value)

        assert listt_1 != listt_2

        self.driver.find_element(By.XPATH, '(//span[@class="mui-style-1sjvzwv"])[5]').click()

        destination = self.driver.find_elements(By.CSS_SELECTOR, 'p[class="MuiTypography-root MuiTypography-body1 hoverText mui-style-12xuhy5"]')

        for i in destination:

            value = i.text

            listt_3.append(value)

        assert listt_3 == listt_1

        

    def chatbot(self):

        time.sleep(7)

        self.driver.find_element(By.CSS_SELECTOR, 'span[class="cc-157aw cc-1kgzy"]').click()

        opening_text = self.driver.find_element(By.CSS_SELECTOR, 'span[class="cc-dvx9d"]').text

        assert opening_text is not None

        self.driver.find_element(By.CSS_SELECTOR, 'textarea[name="message"]').send_keys("Hello")

        self.driver.find_element(By.CSS_SELECTOR, 'textarea[name="message"]').clear()

        self.driver.find_element(By.XPATH, '(//span[@class="cc-ytg1n cc-5t1tm"])[2]').click()

        help_messages = self.driver.find_elements(By.CSS_SELECTOR, 'span[class="cc-5pwnm cc-olo99"]')

        assert help_messages is not None

        self.driver.find_element(By.CSS_SELECTOR, 'input[name="helpdesk_search"]').send_keys("Tourism")

        time.sleep(4)

        results = self.driver.find_elements(By.CSS_SELECTOR, 'span[class="cc-m4qlg cc-361jl"]')

        searchlist = []

        for i in results:

            question = i.text

            assert "Tourism" in question or "tourism" in question

        time.sleep(4)

        self.driver.find_element(By.CSS_SELECTOR, 'span[class="cc-1bvfm"]').click()






        

