import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class MealShare():
    

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')  # create an instance of chrome with driver that's in same directory as this project
        self.driver.implicitly_wait(5) # wait up to 5 seconds for each move

    def load_pastebin(self):
        self.driver.get("https://pastebin.com") # using the .get method to load the website
        self.driver.maximize_window()
        print(self.driver.title)
        

    def input_mealplan(self):
        terms_conditions = self.driver.find_element(By.XPATH, "//button[text()='AGREE']")
        terms_conditions.click()
        pastebinbox = self.driver.find_element(By.NAME, 'PostForm[text]')
        pastebinbox.send_keys('testing')
        sleep(10)

        # search_bar.send_keys(Keys.RETURN)


share_a_meal = MealShare()
share_a_meal.load_pastebin()
share_a_meal.input_mealplan()
