recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}

recipe_2 = {
    "name": "Scrambled Eggs",
    "cooking_time": 10,
    "ingredients": ["Eggs", "Butter", "Salt", "Pepper", "Milk"]
}

recipe_3 = {
    "name": "Spaghetti Bolognese",
    "cooking_time": 30,
    "ingredients": ["Spaghetti", "Ground beef", "Tomato sauce", "Onion", "Garlic", "Parmesan cheese"]
}

recipe_4 = {
    "name": "Chicken Curry",
    "cooking_time": 40,
    "ingredients": ["Chicken", "Curry powder", "Coconut milk", "Onion", "Garlic", "Ginger", "Tomato"]
}

recipe_5 = {
    "name": "Chocolate Cake",
    "cooking_time": 60,
    "ingredients": ["Flour", "Sugar", "Cocoa powder", "Eggs", "Butter", "Milk", "Vanilla extract"]
}

all_recipes = [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]

for recipe in all_recipes:
    print(recipe["ingredients"])
