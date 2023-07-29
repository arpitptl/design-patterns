"""
Template Method design pattern:

The Template Method design pattern is a behavioral pattern that defines the skeleton of an algorithm in a method, allowing subclasses to provide specific implementations for some steps of the algorithm while keeping other steps unchanged.

Let's create an example of the Template Method pattern for a simple recipe application. We'll have an abstract class Recipe representing the template of a cooking recipe, with specific steps such as prepare_ingredients(), cook(), and serve(). Concrete recipe classes like PastaRecipe and CakeRecipe will inherit from Recipe and provide their implementations for the specific steps.
"""

from abc import ABC, abstractmethod

# Abstract Class - Recipe
class Recipe(ABC):
    def prepare_recipe(self):
        self.prepare_ingredients()
        self.cook()
        self.serve()

    @abstractmethod
    def prepare_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass

# Concrete Class - PastaRecipe
class PastaRecipe(Recipe):
    def prepare_ingredients(self):
        print("Gather pasta, sauce, cheese, and spices.")

    def cook(self):
        print("Boil pasta, heat sauce, and mix together.")

    def serve(self):
        print("Serve hot pasta with sauce and cheese.")

# Concrete Class - CakeRecipe
class CakeRecipe(Recipe):
    def prepare_ingredients(self):
        print("Gather flour, sugar, eggs, butter, and baking powder.")

    def cook(self):
        print("Mix ingredients, bake the cake, and let it cool.")

    def serve(self):
        print("Serve delicious cake.")

# Client code
if __name__ == "__main__":
    print("Preparing Pasta Recipe:")
    pasta_recipe = PastaRecipe()
    pasta_recipe.prepare_recipe()

    print("\nPreparing Cake Recipe:")
    cake_recipe = CakeRecipe()
    cake_recipe.prepare_recipe()






"""
In this example, the Recipe class is the abstract class representing the template of a cooking recipe. It has a prepare_recipe() method that defines the algorithm's skeleton, calling the abstract methods prepare_ingredients(), cook(), and serve() in a specific order.

The PastaRecipe and CakeRecipe classes inherit from Recipe and provide their implementations for the abstract methods. They override the prepare_ingredients(), cook(), and serve() methods to define the specific steps needed to prepare pasta and cake recipes.

When the client code prepares a recipe, it calls the prepare_recipe() method of the corresponding recipe object (PastaRecipe or CakeRecipe). The template method prepare_recipe() takes care of the overall flow, while the concrete classes implement the specific steps based on the recipe type.
"""
