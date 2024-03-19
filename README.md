# Exercise 1
## Step 1 - Install Python
Install Python for your operating system and confirm that Python is installed by using the ```python --version``` command in your terminal.

![step1](exercise-1.1/step1.png)

## Step 2 - Set Up a Virtual Environment
Set up the [virtualenvwrapper-win](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) package and then create a new virtual environment named "cf-python-base".

![step2](exercise-1.1/step2.png)

## Step 3 - Create a Python Script
Use your preferred text editor and create a Python script that prompts the user to input two numbers and adds them together, and then run the script from your terminal. The code for this is provided below.

![step3](exercise-1.1/step3.png)

```
# Prompt the user to enter the first number
a = int(input("enter first number: "))

# Prompt the user to enter the second number
b = int(input("enter second number: "))

# Add the two numbers and store the result in variable c
c = a + b

# Print the value of c
print("The sum of", a, "and", b, "is:", c)
```

## Step 4 - Set Up IPython Shell
Install the IPython Shell in the "cf-python-base" environment by running ```pip install ipython```. 
An IPython shell is similar to the regular Python REPL that you saw earlier but with additional features such as syntax highlighting, auto-indentation and robust auto-complete features. 

Verify your installation by launching an IPython shell with the command ```ipython```.

![step4](exercise-1.1/step4.png)

## Step 5 - Export and Use a Requirements File
The requirements file is a text file that lists package requirements for any particular Python application. The requirements file also helps when you’d like to run your Python script on another system. 

First, generate a “requirements.txt” file from the "cf-python-base" environment. To do this, you use the pip freeze command and all packages (including version numbers) installed in the currently activated environment will be compiled: ```pip freeze > requirements.txt```.

Next, create a new environment called “cf-python-copy” by running the command ```mkvirtualenv cf-python-copy```. In this new environment, install packages from the “requirements.txt” file that you generated earlier. 
To install the packages from this file in any other environment, you run the pip install command with the extra -r argument, followed by the name of your requirements file: ```pip install -r requirements.txt```.

![step5](exercise-1.1/step5.png)

# Exercise 2
## Step 1 - Create a structure for ```recipe_1```

The structure needs to contain the following keys:
- name (str): Contains the name of the recipe
- cooking_time (int): Contains the cooking time in minutes
- ingredients (list): Contains a number of ingredients, each of the str data type

For the structure of recipe_1, I would use a dictionary in Python. This is because a dictionary allows for easy association between keys and their corresponding values.

Here's the dictionary structure for the cup of tea recipe:
```
recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}
```

## Step 2 - Create an outer structure called ```all_recipes```, and then add recipe_1 to it.

For the outer structure all_recipes, I would use a list of dictionaries. This allows for sequential storage of multiple recipes while maintaining the flexibility to add, modify, or remove recipes easily.

all_recipes = [recipe_1, ...other recipes]

I've also followed the same structure to create 4 more recipes and add them to the ```all_recipes``` list by using ```all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])```

## Step 3 - Print the ingredients of each recipe as five different lists

We can use a for loop to print the contents of the ingredients key of each recipe:

```
for recipe in all_recipes:
    print(recipe["ingredients"])

# Output
['Tea leaves', 'Sugar', 'Water']
['Eggs', 'Butter', 'Salt', 'Pepper', 'Milk']
['Spaghetti', 'Ground beef', 'Tomato sauce', 'Onion', 'Garlic', 'Parmesan cheese']
['Chicken', 'Curry powder', 'Coconut milk', 'Onion', 'Garlic', 'Ginger', 'Tomato']
['Flour', 'Sugar', 'Cocoa powder', 'Eggs', 'Butter', 'Milk', 'Vanilla extract']
```

# Exercise 1.3

## Step 1 - Initialize two empty lists: recipes_list and ingredients_list

```
recipes_list = []
ingredients_list = []
```

## Step 2 - Define a function called take_recipe, which takes input from the user for the following variables:
- name (str): Stores the name of the recipe.
- cooking_time (int): Stores the cooking time (in minutes).
- ingredients (list): A list that stores ingredients, each of the string data type.
- recipe (dictionary): Stores the name, cooking_time, and ingredients variables (e.g., recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}).

```
def take_recipe():
    name = input("Name of the recipe: ")
    cooking_time = int(input("Cooking time (in minutes): "))
    ingredients = input("Ingredients (ex. Apples, Bananas, ...): ").split(", ")

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    
    return recipe
```

## Step 3 - In the main section of your code, ask the user how many recipes they would like to enter. Their response will be linked to a variable n

```n = int(input("How many recipes would you like to enter? "))```

## Step 4 - Run a for loop, which runs n times to perform the following steps:

- Run take_recipe() and store its return output (a dictionary) in a variable called recipe.
- Run another for loop inside this loop, which iterates through recipe’s ingredients list, where it picks out elements one-by-one as ingredient. It will run the following step inside: if the chosen ingredient isn’t present in ingredients_list, add it to this list. To check if an element ele is present in a sequence seq, you can use the in keyword in a conditional statement as follows: if ele in seq:. Either True or False is returned (remember that you’re checking if ingredient is not in the list, so use the not operator accordingly).
- Once you’ve finished adding ingredients, append recipe to recipes_list.

```
for i in range(0,n):
    print("Recipe", i+1)
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)
```

## Step 5 - Run another for loop that iterates through recipes_list, picks out each element (a dictionary) as recipe, and performs the following steps:

1. Determine the difficulty of the recipe using the following logic:
    - If cooking_time is less than 10 minutes, and the number of ingredients is less than 4, set a variable called difficulty to the value of Easy.
    - If cooking_time is less than 10 minutes, and the number of ingredients is greater than or equal to 4, set a variable called difficulty to the value of Medium.
    - If cooking_time is greater than or equal to 10 minutes, and the number of ingredients is less than 4, set a variable called difficulty to the value of Intermediate.
    - If cooking_time is greater than or equal to 10 minutes, and the number of ingredients is greater than or equal to 4, set a variable called difficulty to the value of Hard.
  
2. Display the recipe in the following format, using values from each dictionary (recipe) obtained from recipes_list:
    ![recipe format](https://images.careerfoundry.com/public/courses/python/A1/1.3/recipe_list-format-code.png)

```
for recipe in recipes_list:
    difficulty = "Easy" if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4 else "Medium" if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4 else "Intermediate" if recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4 else "Hard"

    print("\nRecipe: " + recipe["name"] + "\nCooking Time (min): " + str(recipe["cooking_time"]) + "\nIngredients:")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty level:", difficulty)
```

## Step 6 - Next, you’ll have to display all the ingredients that you’ve come across so far in all of the recipes that you’ve just entered. In Step 5 you appended these ingredients into ingredient_list. Now it’s time to print them all out. Print them in alphabetical order, in a format similar to this example:

![ingredient list format](https://images.careerfoundry.com/public/courses/python/A1/1.3/ingredient_list-example-output.png)

```
print("\nIngredients Available Across All Recipes\n-----------------------------------")
for ingredient in sorted(ingredients_list):
    print(ingredient)
```

# Exercise 1.4

## Part 1 - recipe_input.py script

### Step 1 - Import the pickle and os modules so you can work with binary files and interact with the files in your OS

```
import pickle
import os
```

### Step 2 - Define a function called take_recipe() to take recipes from the user, which performs the following operations:

- Taking in the recipe name, cooking time, and ingredients from the user.
- Calculating the difficulty of the recipe by calling thecalc_difficulty() function.
- Gathering all these attributes into a dictionary and returning it.

```
def take_recipe():
    name = input("Name of the recipe: ")
    cooking_time = int(input("Cooking time (in minutes): "))
    ingredients = input("Ingredients (ex. Apples, Bananas, ...): ").split(", ")
    difficulty = calculate_difficulty(cooking_time, ingredients)

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }

    return recipe
```

### Step 3 - Define the function calc_diffficulty(), where the difficulty is returned as Easy, Medium, Intermediate or Hard

```
def calculate_difficulty(cooking_time, ingredients):
    difficulty = "Easy" if cooking_time < 10 and len(ingredients) < 4 else "Medium" if cooking_time < 10 and len(
        ingredients) >= 4 else "Intermediate" if cooking_time >= 10 and len(ingredients) < 4 else "Hard"

    return difficulty
```

### Step 4 - Have the user enter a filename, which would attempt to open a binary file in read mode. Define a try-except-else-finally block as follows:

1. The try block will open the given file, and load its contents through the pickle module into a variable called data. If the file doesn't exist, the user will have an option to create it. The incoming data is expected to be a dictionary containing two key-value pairs:
    - recipes_list (a list of all recipes)
    - all_ingredients (a list of all ingredients across all recipes)
1. An except clause handles the FileNotFoundError exception if a file with the given name isn’t found. The code block after will create a new dictionary called data, which contains the recipes list under the key recipes_list and another list containing all the ingredients under all_ingredients.
1. Another except clause that handles other exceptions and performs the same operations as the first except block.
1. An else block that closes the file stream that would’ve been opened in the try block.
1. A finally block that extracts the values from the dictionary into two separate lists: recipes_list and all_ingredients.

```
filename = input("Enter the filename of your recipes: ")

try:
    if os.path.isfile("./" + filename):
        file = open(filename, 'rb')
        data = pickle.load(file)

        recipes_list = data["recipes_list"]
        all_ingredients = data["all_ingredients"]
        file.close()
        add_recipe()
    else:
        answer = input(
            "File doesn't exist, would you like to create and use it? (y/n) ")
        if answer == "y":
            add_recipe()
        elif answer == "n":
            print("Quitting...")
        else:
            print("Unrecognized command, quitting script...")

except FileNotFoundError:
    print("File doesn't exist - exiting.")
except:
    print("An unexpected error occurred.")
```

### Step 5 - Ask the user how many recipes they’d like to enter, and define a for loop that calls the take_recipe() function and then define an inner loop that scans through the recipe’s ingredients and adds them to all_ingredients if they’re not already there, then gather the updated recipes_list and all_ingredients into the dictionary called data

```
def add_recipe():
    # Ask user how many recipes they'd like to add
    n = int(input("How many recipes would you like to enter? "))

    # Take input for the number of recipes specified and append to recipe_list
    for i in range(0, n):
        print("Recipe", i+1)
        recipe = take_recipe()

        for ingredient in recipe["ingredients"]:
            if not ingredient in all_ingredients:
                all_ingredients.append(ingredient)

        recipes_list.append(recipe)

    data = {
        "recipes_list": recipes_list,
        "all_ingredients": all_ingredients
    }
```

### Step 6 - Finally, open a binary file with the user-defined filename and write data to it using the pickle module.

```
    file = open(filename, 'wb')
    pickle.dump(data, file)
    print('Data successfully written to "' + filename + '"')
    file.close()
```

## Part 2 - recipe_search.py Script

### Step 1 - Import the pickle module

```import pickle```

### Step 2 - Define a function to display a recipe called display_recipe(), which takes in one recipe (of the dictionary type) as an argument and prints all of its attributes including the recipe name, cooking time, ingredients, and difficulty

```
def display_recipe(recipe):

    print("\nRecipe: " + recipe["name"] + "\nCooking Time (min): " +
          str(recipe["cooking_time"]) + "\nIngredients:")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty level:", recipe["difficulty"])
```

### Step 3 - Define another function called search_ingredient() to search for an ingredient in the given data. The function takes in a dictionary called data as its argument. The function will perform the following steps:

- First, it shows the user all the available ingredients contained in data, under the key all_ingredients. Each ingredient is displayed with a number (take the index of each ingredient for this purpose using the enumerate() function).
- Define a try block where the user gets to pick a number from this list. This number is used as the index to retrieve the corresponding ingredient, which is then stored into a variable called ingredient_searched.
- Make an except clause that warns the user if the input is incorrect.
- Add an else clause that goes through every recipe in data (hint: recipes_list is the key that holds every recipe). Each recipe that contains the given ingredient will be printed.

```
def search_ingredient(data):

    # making a copy of the data object to modify
    data_lower = data.copy()

    # convert all ingredients to lowercase so we can compare them regardless of which case they were originally in
    for recipe in data_lower["recipes_list"]:
        for ingredient in list(enumerate(recipe["ingredients"])):
            recipe["ingredients"][ingredient[0]] = ingredient[1].lower()

    for ingredient in list(enumerate(data_lower["all_ingredients"])):
        data_lower["all_ingredients"][ingredient[0]] = ingredient[1].lower()

    # turn all ingredients into a set which avoids duplicate ingredients, then sort it alphabetically
    all_ingredients = sorted(list(set(data_lower["all_ingredients"])))

    # show a list of all available ingredients
    print("\nAvailable ingredients:")
    for ingredient in list(enumerate(all_ingredients)):
        print(str(ingredient[0]+1) + ": " + ingredient[1])

    # display all recipes that include a user chosen ingredient
    try:
        ingredient_searched = int(input("\nSelect an ingredient from the list by entering its corresponding number: "))
    except:
        print("Invalid input, quitting...")
    else:
        try:
            print('\nList of recipes including ' + '"' +
                  all_ingredients[ingredient_searched - 1] + '":')
            for recipe in list(enumerate(data_lower["recipes_list"])):
                if all_ingredients[ingredient_searched - 1] in recipe[1]["ingredients"]:
                    print("\nRecipe " + str(recipe[0] + 1) + ": " + data["recipes_list"][recipe[0]]["name"] + "\nCooking Time (min): " + str(
                        data["recipes_list"][recipe[0]]["cooking_time"]) + "\nIngredients:")
                    for ingredient in data["recipes_list"][recipe[0]]["ingredients"]:
                        print(ingredient)
                    print("Difficulty level:",
                          data["recipes_list"][recipe[0]]["difficulty"])
        # handle exception where the inputted ingredient index is higher than what exists
        except IndexError:
            print("Item not found, quitting...")
```

### Step 4 - In the main code, ask the user for the name of the file that contains your recipe data

```filename = input("Enter the filename where you've stored your recipes: ")```

### Step 5 - Use a try block to open the file, and then extract its contents into data (from Step 3) using the pickle module. For when the try block fails, add an except block to warn the user that the file hasn’t been found. Define an else block that calls search_ingredient() while passing data into it as an argument.

```
try:
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
except:
    print("An unexpected error occurred.")
else:
    search_ingredient(data)
```

# Exercise 1.5

## Step 1 - Define a class Recipe, with the following data attributes:

- name: the name of a recipe
- ingredients: a list containing the ingredients for a recipe
- cooking_time: the time taken in minutes to carry out a recipe
- difficulty: an auto-generated attribute that says whether the recipe is Easy, Medium, Intermediate, or Hard

```
class Recipe:
    # Class variable to store all ingredients across all recipes
    all_ingredients = set()

    def __init__(self, name):
        # adding an underscore _ before each variable name to indicate that the variable is intended for internal use within the class.
        self._name = name
        self._ingredients = []
        self._cooking_time = None
        self._difficulty = None
```

## Step 2 - Define the following procedural attributes (methods) for the class as well:

- An initialization method that takes in the name for the recipe and initializes the other data attributes too. Getter and setter methods for name and cooking_time.
- A method called add_ingredients that takes in variable-length arguments for the recipe’s ingredients. For example, the arguments could be either ("Salt") or even ("Salt", "Pepper", "Flour", "Water", "Bananas", "Marzipan"); your method should take in these ingredients and add them to ingredients. Once all the ingredients are added, this function calls update_all_ingredients() , which you’ll define shortly.
- A getter method for ingredients that returns the list itself.
- A method called calculate_difficulty() that uses the logic in part 1 of this task, and updates the difficulty of the recipe.
- A getter method for difficulty which also calls calculate_difficulty() if difficulty hasn’t been calculated.
- A search method called search_ingredient() that takes an ingredient as an argument, searches for it in the recipe, and returns True or False appropriately.
- A method called update_all_ingredients() that goes through the current object’s ingredients and adds them to a class variable called all_ingredients, if they’re not already present. This class variable keeps track of all the ingredients that exist across all recipes.
- A string representation that prints the entire recipe over a well formatted string.

```
@property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, value):
        self._cooking_time = value

    # the asterisk before ingredients indicates that the function can accept any number of positional arguments, which will be collected into a tuple.
    def add_ingredients(self, *ingredients):

        # the .extend() method is used to extend an existing list by appending elements from another iterable object, (in this case the ingredients tuple), 
        # such as a list, tuple, set, or any other iterable.
        self._ingredients.extend(ingredients)
        self.update_all_ingredients()

    @property
    def ingredients(self):
        return self._ingredients

    def calculate_difficulty(self):
        if self._cooking_time is None or self._ingredients is None:
            return
        if self._cooking_time < 10 and len(self._ingredients) < 4:
            self._difficulty = "Easy"
        elif self._cooking_time < 10 and len(self._ingredients) >= 4:
            self._difficulty = "Medium"
        elif self._cooking_time >= 10 and len(self._ingredients) < 4:
            self._difficulty = "Intermediate"
        else:
            self._difficulty = "Hard"

    @property
    def difficulty(self):
        # using the keyword "is" tests if two variables point to the same object instead of if they just have the same value
        # for example it would return false for these two lists: a = [1,2,3]; b = [1,2,3] as they point to different objects in memory
        if self._difficulty is None:
            self.calculate_difficulty()
        return self._difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self._ingredients

    def update_all_ingredients(self):
        # The .update() method is primarily used to update the contents of a dictionary or set with the elements from another iterable object,
        # such as another dictionary, a list, or a set.
        #
        # In the case of sets like the Recipe class' shared "all_ingredients" set, the .update() method
        # adds elements from another iterable (self._ingredients) to the set.
        # If the elements (ingredients in this case) already exist in the set, they are ignored.
        Recipe.all_ingredients.update(self._ingredients)

    def __str__(self):
        # using f-strings, or formatted string literals for interpolation and easier formatting
        return f"{self._name}:\nIngredients: {', '.join(self._ingredients)}\nCooking time: {self._cooking_time} minutes\n"
```

## Step 3 - To find recipes that contain a specific ingredient, define a method called recipe_search():

1. Define 2 parameters for this method:
    - data: takes in a list of Recipe objects to search from
    - search_term: the ingredient to be searched for
1. Run a for loop that traverses through data, and performs the following steps:
    - Within the object that is in focus, call the search_ingredient method to see if the ingredient is present or not.
    - If the above condition is satisfied, print the recipe.

```
# Method used to find recipes that contain a specific ingredient
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
```

## Step 4 - In the main code, make an object under the Recipe class:

- Initialize an object named tea under this class, and set the recipe’s name as "Tea" through the initialization step.
- Add the following ingredients to this recipe: Tea Leaves, Sugar, Water.
- Set the cooking time for this recipe as 5 (in minutes).
- Display the string representation of this object.
 
```
# Creating recipe objects
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.cooking_time = 5
```

## Step 5 - Make a few more recipes with the given attributes, and display their respective string representations as well:

1. Coffee:
    - Ingredients: Coffee Powder, Sugar, Water
    - Cooking time: 5 minutes
2. Cake:
    - Ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
    - Cooking time: 50 minutes
3. Banana Smoothie:
    - Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
    - Cooking time: 5 minutes

```
coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.cooking_time = 5

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs",
                     "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.cooking_time = 50

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.cooking_time = 5

# Displaying string representations
print("String representations of a recipe:\n" + 30*"-")
print(tea)
print(coffee)
print(cake)
print(banana_smoothie)
print(30*"-")
```

## Step 6 - Wrap the recipes into a list called recipes_list.

```
# Creating a list of recipes
recipes_list = [tea, coffee, cake, banana_smoothie]
```

## Step 7 - Use the recipe_search() method to search for recipes that contain each ingredient out of: Water, Sugar, Bananas.

```
# Using recipe_search method to search for recipes containing specific ingredients
ingredients_to_search = ["Water", "Sugar", "Bananas"]
for ingredient in ingredients_to_search:
    print(f"Recipes containing {ingredient}:")
    recipe_search(recipes_list, ingredient)
    # print newline character at the end for better formatting
    print()
```

## Final output:

```
String representations of a recipe:
------------------------------
Tea:
Ingredients: Tea Leaves, Sugar, Water
Cooking time: 5 minutes

------------------------------
Recipes containing Water:
Tea:
Ingredients: Tea Leaves, Sugar, Water
Cooking time: 5 minutes

Coffee:
Ingredients: Coffee Powder, Sugar, Water
Cooking time: 5 minutes


Recipes containing Sugar:
Tea:
Ingredients: Tea Leaves, Sugar, Water
Cooking time: 5 minutes

Coffee:
Ingredients: Coffee Powder, Sugar, Water
Cooking time: 5 minutes

Cake:
Ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk

Recipes containing Bananas:
Banana Smoothie:
Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
Cooking time: 5 minutes
```

# Exercise 1.6

## Part 1: Create & Connect Database

Before you visualize anything to the user, you should connect your “recipe_mysql.py” script to your MySQL server:

1. First, import the mysql.connector module.

```import mysql.connector```

2. Next, initialize a connection object called conn, which connects with the following parameters, based on the user that you set up earlier:

    - Hostname is localhost
    - Username is cf-python
    - Password is password

```
def connect_to_database():
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="cf-python",
        password="password"
    )
```

3. Next, initialize a cursor object from conn.

```
    # Create a cursor object
    cursor = conn.cursor()
```

4. Create a database called task_database. To ensure you don’t get errors from accidentally using multiple databases with the same name, make sure it’s the only database with this name on the server by using the EXISTS statement: CREATE DATABASE IF NOT EXISTS <database name>

```
    # Create task_database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
```

5. Have your script access your database with the USE statement.

```
    # Use task_database
    cursor.execute("USE task_database")
```

6. Create a table called Recipes with the following columns:
    - id: integer type; increments automatically; the primary key for this table.
    - name: string type; character limit of 50; stores the name of the recipe.
    - ingredients: string type; character limit of 255; stores the ingredients of the recipe in the form of a string.
    - cooking_time: integer type; stores the cooking time in minutes.
    - difficulty: string type; character limit of 20; stores the difficulty level as Easy, Medium, Intermediate, or Hard.

As you did with the database, use the EXISTS statement to make sure there isn’t already a table with the same name: CREATE TABLE IF NOT EXISTS <table name>

```
    # Create Recipes table if not exists
    cursor.execute("CREATE TABLE IF NOT EXISTS Recipes (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), ingredients VARCHAR(255), cooking_time INT, difficulty VARCHAR(20))")

    return conn, cursor
```

## Part 2: The Main Menu

To implement a main menu, let’s first understand how the user would flow through it:

- First, the user gets to choose from four options: adding recipes, searching for recipes, modifying recipes, and deleting recipes. Once the user selects an option, it should be launched through its own function call. When the function is over, the user needs to be taken back to the main menu so they can perform other operations.
- The process of user selection, function calling, and returning to the main menu requires a loop so that after the process has been completed once it can loop and happen again. A while loop would be perfect for this, because in this case you don’t know exactly how many times the loop will run.
- The condition for running the loop can be based on the user’s choice between the 4 options (adding recipes, searching for recipes, etc.). However, if the user were to enter a designated choice to exit the program, the loop would stop.

Therefore, your main_menu() function requires the following options:

1. Creating a new recipe: Calls a function called create_recipe() which accepts conn and cursor as its arguments.
2. Searching for a recipe by ingredient: Calls a function called search_recipe() which accepts conn and cursor as its arguments.
3. Updating an existing recipe: Calls a function called update_recipe() which accepts conn and cursor as its arguments.
4. Deleting a recipe: Calls a function called delete_recipe() which accepts conn and cursor as its arguments.

If the user exits this loop, any changes to the database would be committed and the connection created would be closed.

Once you've defined the main_menu() function, call it in the main code. Pass conn and cursor as arguments so that the code inside the main_menu() function can use the database.

```
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
```

## Part 3: Creating a Recipe with create_recipe()

1. First, collect the following details for a recipe entry:
    - name: Name of the recipe, string type.
    - cooking_time: Cooking time of the recipe in minutes, integer type.
    - ingredients: Ingredients of the recipe, each ingredient stored as a string in this list.

```
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (minutes): "))
    ingredients = input(
        "Enter ingredients (comma-separated, ex: water,sugar): ").split(',')
```

2. Next, call a function called calculate_difficulty(). It calculates the difficulty of the recipe by taking in cooking_time and ingredients as its arguments, and returning one of the following strings: Easy, Medium, Intermediate, or Hard. Store the output in a variable called difficulty.

```
    difficulty = calculate_difficulty(cooking_time, ingredients)

# outside of create_recipe()
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"
```

3. Now, you have to prepare to wrap this information up in an SQL query so that you can enter it into the Recipes table on your database. Since MySQL doesn’t fully support arrays, your ingredients list needs to be converted into a comma-separated string. This can be done through the join() method, which is used with the syntax: <returned_string> = "<separator characters>".join(<sequence from which items are to be joined>). Here, you need to join the elements of the list ingredients, the separator being a comma followed by a space (", "). Finally, build the query string in the following format: INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (<respective values for each column>).

```
    ingredients_string = ", ".join(ingredients)

    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
```

4. Execute the query, then commit your changes.

```
    cursor.execute(query, (name, ingredients_string, cooking_time, difficulty))
    conn.commit()
    print("Recipe created successfully!")
```

## Part 4: Searching for a Recipe with search_recipe()

1. You need to begin with an entire list of ingredients that is available in the Recipes table for the user to choose from. Obtain this list by SELECT-ing only the ingredients column from your table. Store the output into a variable called results.

```
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
```

2. results is made up of a list of rows, each row being a tuple containing column values. Since you’re only retrieving the ingredients column, each row contains a single-element tuple, the element being a string containing the ingredients for each recipe. Add each ingredient that you come across into a new list called all_ingredients, and make sure that there are no duplicates.

```
    all_ingredients = set()
    for result in results:
        ingredients = result[0].split(',')
        all_ingredients.update(ingredients)
```

3. Display all the ingredients that you’ve found so far to the user, and allow them to pick a number corresponding to the ingredient in order to begin a search. Store the ingredient to be searched for into a variable called search_ingredient.

```
    print("Available ingredients:")
    for index, ingredient in enumerate(all_ingredients, 1):
        print(f"{index}. {ingredient}")

    search_index = int(
        input("\nEnter the number corresponding to the ingredient you want to search: "))
    search_ingredient = list(all_ingredients)[search_index - 1]
```

4. To search for rows in the table that contain search_ingredient within the ingredients column, use the WHERE statement with the LIKE operator: ```SELECT <columns to be displayed> FROM <table> WHERE <search column> LIKE <search pattern>```.

In your case, an ingredient that you search for can either be in the middle, at the beginning, or at the end of the ingredients string. SQL Server supports the wildcard %, which represents zero or more characters in its position. Hence, if you’re searching for beans within a string, your search pattern should be %beans%.


```
    query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(query, ('%' + search_ingredient + '%',))
```

5. Use this logic to build your query, fetch the results that satisfy this condition, and display them to the user.

```
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
```

## Part 5: Updating a Recipe with update_recipe()

1. In this function, you’ll first fetch all the recipes that are present on the database and list them to the user. The user will then pick a recipe to be updated by specifying its corresponding id, after which the script will ask for the column to be updated for that recipe. The columns available for modification are name, cooking_time and ingredients.

```
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
```

2. Once the user selects the column that needs an update, collect the new value from the user.

```
    recipe_id = int(input("Enter the ID of the recipe you want to update: "))
    column_name = input(
        "Enter the column to update (name, cooking_time, ingredients): ")
    new_value = input(
        "Enter the new value (ex: text for name, number for cooking_time, and text separated by commas for ingredients): ")
```

3. Build your query in the form of a string, to update an entry on the table for the given id, column, and updated value. Note that if the user is updating either cooking_time or ingredients, the script will have to recalculate the difficulty of the recipe, then update that column as well (make a separate query for this), then execute your queries on the table and commit your changes.

```
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
```

## Part 6: Deleting a Recipe with delete_recipe()

1. This function will display every recipe in your table to the user, where they can pick one by its id for deletion.

```
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
```

2. Build a query using the DELETE statement, where the row to be deleted is identified by the id that the user had specified, the execute this query and commit your changes to the table.

```
    query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(query, (recipe_id,))

    conn.commit()
    print("Recipe deleted successfully!")
```

## Part 7: Screenshots of finished program

1. Save your Python script and ensure that your MySQL server is running on your system. Then, run your script.

2. Create about 3 to 4 simple recipes of your choice using the first option in your menu: Create a Recipe.

![step1](exercise-1.6/step1.png)

3. Run a search by selecting the ingredient to search for, this time using the second option in your script: Search for a Recipe.

![step2](exercise-1.6/step2.png)

4. Change a few values in some of your recipes using the third option in your script’s menu: Update a Recipe. 2 or 3 updates should be enough.

![step3](exercise-1.6/step3.png)

5. Delete any one of your recipes using the final option: Delete a Recipe.

![step4](exercise-1.6/step4.png)

6. Exit the script using the exit keyword that you defined before (e.g. quit).

![step5](exercise-1.6/step5.png)



