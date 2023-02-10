import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


from meal_generator import MealGenerator


class MealShare():
    

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')  # create an instance of chrome with driver that's in same directory as this project
        self.driver.implicitly_wait(5) # wait up to 5 seconds for each move


    def load_pastebin(self):
        self.driver.get("https://pastebin.com") # using the .get method to load the website
        self.driver.maximize_window()
        sleep(2)
        

    def input_mealplan(self):
        terms_conditions = self.driver.find_element(By.XPATH, "//button[text()='AGREE']")
        terms_conditions.click()
        pastebinbox = self.driver.find_element(By.NAME, 'PostForm[text]')
        pastebinbox.send_keys(f'Shopping list for this week:\n{MealGenerator().generate_meal()}')
        print('Meal plan added to pastebin.')
        
    def navigate_dropdowns(self):
        open_categories = self.driver.find_element(By.CLASS_NAME, "select2-selection__arrow")
        open_categories.click()
        choose_food_category = self.driver.find_element(By.XPATH, "//li[text()='Food']")
        choose_food_category.click()
        sleep(5)
        
        self.driver.execute_script("window.scrollTo(0, 100)") 
        
        open_paste_expiration = self.driver.find_element(By.CLASS_NAME, "select2-selection__arrow") # class names are the same, how to find element by finding ajacent element?
        open_paste_expiration.click()
        choose_paste_expiration = self.driver.find_element(By.XPATH, "//li[text()='1 Hour']")
        choose_paste_expiration.click()

    def naming_new_paste(self):
        create_paste_title = self.driver.find_element(By.NAME, 'PostForm[name]')
        create_paste_title.send_keys('Meal plan shopping list')
        sleep(3)
        create_new_paste = self.driver.find_element(By.XPATH, "//button[text()='Create New Paste']")
        # create_new_paste.click()
        sleep(5)


share_a_meal = MealShare()
share_a_meal.load_pastebin()
share_a_meal.input_mealplan()
share_a_meal.navigate_dropdowns()
share_a_meal.naming_new_paste()

#This string works<bound method MealGenerator.generate_meal of <meal_generator.MealGenerator object at 0x7fed66271f70>>
