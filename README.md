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
