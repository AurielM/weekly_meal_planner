from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from meal_generator import MealGenerator


class MealShare:
    def __init__(self):
        """
        This class takes the meal plan produced by the MealGenerator
        and produces a link (printed in the terminal)through which the shopping list for this meal plan can be shared
        """

        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.implicitly_wait(5)

    def load_pastebin(self):
        self.driver.get("https://pastebin.com")
        self.driver.maximize_window()
        sleep(2)

    def input_mealplan(self):
        terms_conditions = self.driver.find_element(By.XPATH, "//button[text()='AGREE']")
        terms_conditions.click()
        pastebinbox = self.driver.find_element(By.NAME, "PostForm[text]")
        pastebinbox.send_keys(f"Shopping list for this week:\n{MealGenerator().generate_meal()}")

    def navigate_dropdowns(self):
        open_categories = self.driver.find_element(By.CLASS_NAME, "select2-selection__arrow")
        open_categories.click()
        choose_food_category = self.driver.find_element(By.XPATH, "//li[text()='Food']")
        choose_food_category.click()
        sleep(5)

        self.driver.execute_script("window.scrollTo(0, 100)")

        open_paste_expiration = self.driver.find_elements(By.CLASS_NAME, "select2-selection__arrow")[2]
        open_paste_expiration.click()
        choose_paste_expiration = self.driver.find_element(By.XPATH, "//li[text()='1 Hour']")
        choose_paste_expiration.click()

    def naming_new_paste(self):
        create_paste_title = self.driver.find_element(By.NAME, "PostForm[name]")
        create_paste_title.send_keys("Meal plan shopping list")
        create_new_paste = self.driver.find_element(By.XPATH, "//button[text()='Create New Paste']")
        create_new_paste.click()

    def produce_URL_to_share(self):
        current_url = self.driver.current_url
        print(f"\nLink of meal_plan here: {current_url}")
        sleep(5)


share_a_meal = MealShare()
share_a_meal.load_pastebin()
share_a_meal.input_mealplan()
share_a_meal.navigate_dropdowns()
share_a_meal.naming_new_paste()
share_a_meal.produce_URL_to_share()
