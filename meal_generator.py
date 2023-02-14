from meals import meals_vs_ingredients
import random


class MealGenerator():


    def __init__(self):
        self.single_meal = 0
        self.shopping_list = []
        self.meal_plan = set()
        self.required_ingredients = []


    def meal_and_ingredients(self, meal_plan):
        for meal in meal_plan:
            # print(f"\nMeal: {meal}")
            self.required_ingredients = meals_vs_ingredients[meal]
            self.shopping_list.extend(self.required_ingredients)
        return self.shopping_list


    def create_meal_plan(self):
        while len(self.meal_plan) < 2:
            key = random.choice(list(meals_vs_ingredients.keys()))
            self.meal_plan.add(key)
        return self.meal_plan


    def final_shopping_list(self, shopping_list):
        formatted_shopping_list = ""
        for item in shopping_list:
            if item in formatted_shopping_list:
                pass
            else:
                formatted_shopping_list += item + '\n'
        return formatted_shopping_list


    def generate_meal(self):
        return self.final_shopping_list(self.meal_and_ingredients(self.create_meal_plan()))
