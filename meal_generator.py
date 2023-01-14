from meals import meals_vs_ingredients
import random


single_meal = 0
shopping_list = []
meal_plan = set()


while len(meal_plan) < 2:
    key, value = random.choice(list(meals_vs_ingredients.items()))
    meal_plan.add(key)
for meal in meal_plan:
    print(f"{meal} : Meal")
    required_ingredients = meals_vs_ingredients[meal]
    for ingredient in required_ingredients:
        print(ingredient)
    print()