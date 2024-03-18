class Recipe:
    # Class variable to store all ingredients across all recipes
    all_ingredients = set()

    def __init__(self, name):
        # adding an underscore _ before each variable name to indicate that the variable is intended for internal use within the class.
        self._name = name
        self._ingredients = []
        self._cooking_time = None
        self._difficulty = None

    # using @property and @name.setter decorator to specify getter and setter methods for each variable
    # it allows you to access a method like an attribute, without the need for parentheses (ex. obj.x)
    # this is useful when you want to expose attributes of an object but need to perform some computation or validation when accessing them
    #
    # @name.setter is used in conjunction with @property to define both getter and setter for a property
    # the name inside @name.setter should match the name of the property defined with @property

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

# Method used to find recipes that contain a specific ingredient
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


# Creating recipe objects
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.cooking_time = 5

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

# Creating a list of recipes
recipes_list = [tea, coffee, cake, banana_smoothie]

# Using recipe_search method to search for recipes containing specific ingredients
ingredients_to_search = ["Water", "Sugar", "Bananas"]
for ingredient in ingredients_to_search:
    print(f"Recipes containing {ingredient}:")
    recipe_search(recipes_list, ingredient)
    # print newline character at the end for better formatting
    print()
