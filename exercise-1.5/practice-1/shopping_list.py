class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []
        
    def add_item(self, item):
        if not item in self.shopping_list:
            self.shopping_list.append(item)
            print("Item added to shopping list")
        else:
            print("Item is already in shopping list")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print("Item removed from shopping list")
        else:
            print("Item is not in shopping list")

    def view_list(self):
        print("\n"+self.list_name)
        print(self.shopping_list)

pet_store_list = ShoppingList("Pet Store Shopping List")
pet_store_list.add_item("Dog food")
pet_store_list.add_item("Frisbee")
pet_store_list.add_item("Bowl")
pet_store_list.add_item("Collars")
pet_store_list.add_item("Flea collars")

pet_store_list.remove_item("Flea collars")

pet_store_list.add_item("Frisbee")

pet_store_list.view_list()
