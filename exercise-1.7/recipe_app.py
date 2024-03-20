import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Part 1: Set Up Your Script & SQLAlchemy

# MySQL database credentials
username = "cf-python"
password = "password"
hostname = "localhost"
database_name = "task_database"

# Connect to the MySQL database
engine = create_engine(
    f"mysql://{username}:{password}@{hostname}/{database_name}")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Part 2: Create Your Model and Table


class Recipe(Base):
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe(id={self.id}, name='{self.name}', difficulty='{self.difficulty}')>"

    def __str__(self):
        return f"Recipe ID: {self.id}\nName: {self.name}\nIngredients: {self.ingredients}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.difficulty}\n"

    def calculate_difficulty(self):

        ingredient_count = len(self.return_ingredients_as_list())

        if self.cooking_time < 10 and ingredient_count < 4:
            difficulty_level = "Easy"
        elif self.cooking_time < 10 and ingredient_count >= 4:
            difficulty_level = "Medium"
        elif self.cooking_time >= 10 and ingredient_count < 4:
            difficulty_level = "Intermediate"
        else:
            difficulty_level = "Hard"
            
        self.difficulty = difficulty_level

    # function to convert ingredients from string to a list
    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        else:
            return self.ingredients.split(', ')


# Create the table
Base.metadata.create_all(engine)


# Part 3: Define your Main Operations as Functions

def create_recipe():
    # Get recipe name with input error checking
    while True:
        name = input("Enter recipe name: ")
        if len(name) > 50:
            print("Recipe name must not exceed 50 characters.")
        else:
            break

    # Get number of ingredients
    while True:
        try:
            ingredients_count = int(input("Enter the number of ingredients: "))
            break
        except ValueError:
            print("Please enter a valid number for the ingredients count.")

    # Get ingredients with input error checking
    ingredients = []
    for i in range(ingredients_count):
        while True:
            ingredient = input(f"Enter new ingredient {i+1}: ")
            ingredients.append(ingredient)
            if len(", ".join(ingredients)) > 255:
                print("Ingredient list must not exceed 255 characters. Current character count: " + str(len(", ".join(ingredients))))
                ingredients.pop()
            else:
                break

    ingredients_str = ', '.join(ingredients)

    # Get cooking time with input error checking
    while True:
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
            break
        except ValueError:
            print("Cooking time must be a valid integer.")

    recipe_entry = Recipe(name=name, ingredients=ingredients_str, cooking_time=cooking_time)
    recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()
    print("Recipe added successfully!")


def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return
    
    print("\nAll available recipes:")
    print(30*"-")
    for recipe in recipes:
        print(recipe)

def search_by_ingredients():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return

    all_ingredients = []
    for recipe in recipes:
        ingredients_list = recipe.return_ingredients_as_list()
        all_ingredients.extend(ingredients_list)

    unique_ingredients = list(set(all_ingredients))

    print("\nAvailable ingredients:")
    print(30*"-")
    for i, ingredient in enumerate(unique_ingredients, 1):
        print(f"{i}. {ingredient}")

    while True:
        user_input = input("\nEnter ingredient numbers separated by spaces: ")
        input_numbers = user_input.split()

        # Check if all input values are valid numbers within the available options
        if all(number.isdigit() and 1 <= int(number) <= len(unique_ingredients) for number in input_numbers):
            search_ingredients = [unique_ingredients[int(i)-1] for i in input_numbers]
            break
        else:
            print("Invalid input. Please enter valid ingredient numbers.")

    conditions = []
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))

    filtered_recipes = session.query(Recipe).filter(*conditions).all()

    print('\nRecipes including "' + ", ".join(search_ingredients) + '"')
    print(30*"-")
    for recipe in filtered_recipes:
        print(recipe)


def edit_recipe():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return

    print("\nAvailable recipes:")
    for recipe in recipes:
        print(f"{recipe.id}. {recipe.name}")

    recipe_id = int(input("\nEnter the ID of the recipe you want to edit: "))
    recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_edit:
        print("Invalid recipe ID.")
        return

    # print(recipe_to_edit)
    print("\nType the number corresponding to the attribute you'd like to edit: ")
    print(f"1. Name ({recipe_to_edit.name})")
    print(f"2. Ingredients ({recipe_to_edit.ingredients})")
    print(f"3. Cooking Time ({recipe_to_edit.cooking_time})")
    attribute_choice = input("\nEnter your choice: ")

    # Editing name
    if attribute_choice == "1":
        while True:
            new_name = input("Enter the new name: ")
            if len(new_name) > 50:
                print("Recipe name must not exceed 50 characters.")
            else:
                break

    # Editing ingredients
    elif attribute_choice == "2":
    # Get number of ingredients
        while True:
            try:
                new_ingredients_count = int(input("Enter the number of new ingredients: "))
                break
            except ValueError:
                print("Please enter a valid number for the ingredients count.")

        # Get ingredients with input error checking
        new_ingredients = []
        for i in range(new_ingredients_count):
            while True:
                ingredient = input(f"Enter new ingredient {i+1}: ")
                new_ingredients.append(ingredient)
                if len(", ".join(new_ingredients)) > 255:
                    print("Ingredient list must not exceed 255 characters. Current character count: " + str(len(", ".join(new_ingredients))))
                    new_ingredients.pop()
                else:
                    break

        new_ingredients_str = ', '.join(new_ingredients)
        recipe_to_edit.ingredients = new_ingredients_str

    # Editing cooking time
    elif attribute_choice == "3":
    # Get cooking time with input error checking
        while True:
            try:
                new_cooking_time = int(input("Enter the new cooking time (in minutes): "))
                break
            except ValueError:
                print("Cooking time must be a valid integer.")

        recipe_to_edit.cooking_time = new_cooking_time

    else:
        print("Invalid choice.")
        return

    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("Recipe updated successfully!")

def delete_recipe():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return

    print("Available recipes:")
    for recipe in recipes:
        print(f"{recipe.id}. {recipe.name}")

    recipe_id = int(input("\nEnter the ID of the recipe you want to delete: "))
    recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_delete:
        print("Invalid recipe ID.")
        return

    while True:
        confirmation = input(
            f"\nAre you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ")
        if confirmation.lower() == 'yes':
            session.delete(recipe_to_delete)
            session.commit()
            print("\nRecipe deleted successfully!")
            break
        elif confirmation.lower() == 'no':
            print("\nDeletion canceled.")
            break
        else:
            print("\nPlease enter a valid answer (yes/no)")
    

# Part 4: Design Your Main Menu

while True:
    print("\nMain Menu:")
    print("1. Create a new recipe")
    print("2. View all recipes")
    print("3. Search for recipes by ingredients")
    print("4. Edit a recipe")
    print("5. Delete a recipe")
    print("Type 'quit' to quit the application")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        create_recipe()
    elif choice == "2":
        view_all_recipes()
    elif choice == "3":
        search_by_ingredients()
    elif choice == "4":
        edit_recipe()
    elif choice == "5":
        delete_recipe()
    elif choice.lower() == "quit":
        break
    else:
        print("Invalid choice. Please try again.")
        continue

session.close()
engine.dispose()
