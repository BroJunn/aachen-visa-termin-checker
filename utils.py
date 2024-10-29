from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from config import *
import time



class Checker:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def init_url_root(self, url_root: str):
        try:
            self.driver.get(url_root)
        except NoSuchWindowException:
            self.driver = webdriver.Chrome()
            self.driver.get(url_root)

    def click_to_verlaengen(self, idx_group: int):

        button1 = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "buttonfunktionseinheit-1"))
        )
        button1.click()

        try:
            cookie_msg_div = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "cookie_msg")))
            cookie_close_button = self.driver.find_element(by=By.ID, value="cookie_msg_btn_no")
            cookie_close_button.click()
        except TimeoutException:
            print('no cookie setting message')

        button2 = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, BUTTON_ID_AUFFENHALT))
        )
        button2.click()

        if idx_group == 1:
            button3 = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, BUTTON_ID_TEAM1))
            )
            button3.click()
        elif idx_group == 2:
            button4 = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, BUTTON_ID_TEAM2))
            )
            button4.click()
        elif idx_group == 3:
            button5 = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, BUTTON_ID_TEAM3))
            )
            button5.click()
        else:
            raise NotImplementedError

        try:
            cookie_msg_div = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "cookie_msg")))
            cookie_close_button = self.driver.find_element(by=By.ID, value="cookie_msg_btn_no")
            cookie_close_button.click()
        except TimeoutException:
            print('no cookie setting message')

        weiter_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "WeiterButton"))
        )
        weiter_button.click()

        ok_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "OKButton"))
        )
        ok_button.click()

        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-primary.onehundred.pull-right"))
        )
        continue_button.click()
        time.sleep(3)

    def check_if_no_appointment(self):
        try:
            self.driver.find_element(By.XPATH, "//h2[@class='h1like' and contains(text(), 'Kein freier Termin verfügbar')]")
            return True
        except NoSuchElementException:
            return False
    