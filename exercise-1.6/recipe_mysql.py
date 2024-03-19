import mysql.connector


def connect_to_database():
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="cf-python",
        password="password"
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Create task_database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

    # Use task_database
    cursor.execute("USE task_database")

    # Create Recipes table if not exists
    cursor.execute("CREATE TABLE IF NOT EXISTS Recipes (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), ingredients VARCHAR(255), cooking_time INT, difficulty VARCHAR(20))")

    return conn, cursor


def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (minutes): "))
    ingredients = input(
        "Enter ingredients (comma-separated, ex: water,sugar): ").split(',')
    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients_string = ", ".join(ingredients)

    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, ingredients_string, cooking_time, difficulty))
    conn.commit()
    print("Recipe created successfully!")


def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"


def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = set()
    for result in results:
        ingredients = result[0].split(',')
        all_ingredients.update(ingredients)

    print("Available ingredients:")
    for index, ingredient in enumerate(all_ingredients, 1):
        print(f"{index}. {ingredient}")

    search_index = int(
        input("\nEnter the number corresponding to the ingredient you want to search: "))
    search_ingredient = list(all_ingredients)[search_index - 1]

    query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(query, ('%' + search_ingredient + '%',))
    search_results = cursor.fetchall()

    print("Search Results:")
    print(30*"-")
    for recipe in search_results:
        print("ID:", recipe[0])
        print("Name:", recipe[1])
        print("Ingredients:", recipe[2])
        print("Cooking time:", recipe[3], "minutes")
        print("Difficulty:", recipe[4])
        print()
    print(30*"-")


def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()

    print("Available recipes:")
    print(30*"-")
    for recipe in recipes:
        print("ID:", recipe[0])
        print("Name:", recipe[1])
        print("Ingredients:", recipe[2])
        print("Cooking time:", recipe[3], "minutes")
        print("Difficulty:", recipe[4])
        print()
    print(30*"-")

    recipe_id = int(input("Enter the ID of the recipe you want to update: "))
    column_name = input(
        "Enter the column to update (name, cooking_time, ingredients): ")
    new_value = input(
        "Enter the new value (ex: text for name, number for cooking_time, and text separated by commas for ingredients): ")

    if column_name == 'cooking_time':
        # Fetch the current list of ingredients from the database
        cursor.execute(
            "SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        current_ingredients = cursor.fetchone()[0].split(',')

        # Recalculate difficulty using the new cooking time and current ingredients
        new_difficulty = calculate_difficulty(new_value, current_ingredients)
    else:
        # Fetch the current cooking time from the database
        cursor.execute(
            "SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        current_cooking_time = cursor.fetchone()[0]

        # Recalculate difficulty using the current cooking time and new ingredients
        new_difficulty = calculate_difficulty(current_cooking_time, new_value)

    # Update the difficulty in the database
    cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s",
                   (new_difficulty, recipe_id))

    query = f"UPDATE Recipes SET {column_name} = %s WHERE id = %s"
    cursor.execute(query, (new_value, recipe_id))

    conn.commit()
    print("Recipe updated successfully!")


def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()

    print("Available recipes:")
    print(30*"-")
    for recipe in recipes:
        print("ID:", recipe[0])
        print("Name:", recipe[1])
        print("Ingredients:", recipe[2])
        print("Cooking time:", recipe[3], "minutes")
        print("Difficulty:", recipe[4])
        print()
    print(30*"-")

    recipe_id = int(input("Enter the ID of the recipe you want to delete: "))

    query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(query, (recipe_id,))

    conn.commit()
    print("Recipe deleted successfully!")


def main_menu(conn, cursor):
    while True:
        print("\nMain Menu:")
        print("1. Create a Recipe")
        print("2. Search for a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    conn, cursor = connect_to_database()
    main_menu(conn, cursor)
