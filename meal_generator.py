from meals import meals_vs_ingredients
import random


single_meal = 0
shopping_list = []
meal_plan = set()


while len(meal_plan) < 2:
    key, value = random.choice(list(meals_vs_ingredients.items()))
    meal_plan.add(key)
print(f'\nThis week\'s meal plan {list(meal_plan)}')
for meal in meal_plan:
    print(f"\nMeal: {meal}")
    required_ingredients = meals_vs_ingredients[meal]
    for ingredient in required_ingredients:
        print(f'- {ingredient}')
    shopping_list.extend(required_ingredients)
print(f'\nFinal shopping list ({len(shopping_list)} items):\n{shopping_list}')