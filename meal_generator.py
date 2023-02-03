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
            print(f"\nMeal: {meal}")
            self.required_ingredients = meals_vs_ingredients[meal]
            self.shopping_list.extend(self.required_ingredients)
            for self.ingredient in self.required_ingredients:
                print(f'- {self.ingredient}')
        return self.shopping_list


    def create_meal_plan(self):
        while len(self.meal_plan) < 2:
            key = random.choice(list(meals_vs_ingredients.keys()))
            self.meal_plan.add(key)
        print(f'\nThis week\'s meal plan {list(self.meal_plan)}')
        return self.meal_plan

        
    def final_shopping_list(self, shopping_list):
        print(f'\nFinal shopping list ({len(shopping_list)} items):\n')
        for item in shopping_list:
            print(item)


week1 = MealGenerator
week1().final_shopping_list(week1().meal_and_ingredients(week1().create_meal_plan()))