"""
Decorator design pattern:

The Decorator design pattern allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects from the same class. It is achieved by creating a set of decorator classes that wrap the original class, adding new functionalities while preserving the original class's interface. Here's an example of the Decorator pattern in Python:

Let's create a simple coffee ordering system where we have a Coffee class representing the base coffee and several decorator classes representing different add-ons.
"""

# Component (Base Coffee) class
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Simple Coffee"

# Concrete Component class
class Espresso(Coffee):
    def cost(self):
        return 8

    def description(self):
        return "Espresso"

# Decorator class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

# Concrete Decorator class
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2

    def description(self):
        return super().description() + ", Milk"

# Concrete Decorator class
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1

    def description(self):
        return super().description() + ", Sugar"

# Example usage
if __name__ == "__main__":
    coffee = Espresso()
    print(f"Cost: ${coffee.cost()}, Description: {coffee.description()}")

    coffee_with_milk = MilkDecorator(coffee)
    print(f"Cost: ${coffee_with_milk.cost()}, Description: {coffee_with_milk.description()}")

    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(f"Cost: ${coffee_with_milk_and_sugar.cost()}, Description: {coffee_with_milk_and_sugar.description()}")




"""
In this example, we have a Coffee class representing the base coffee. The Espresso class is a concrete coffee type that inherits from Coffee.

The CoffeeDecorator class is the base decorator class, which also inherits from Coffee. It contains a reference to the Coffee object it decorates. Concrete decorator classes (MilkDecorator and SugarDecorator) inherit from CoffeeDecorator and add their own functionalities.

The decorators modify the cost and description of the original coffee based on the add-ons they provide. By stacking multiple decorators, we can add multiple functionalities to the original coffee dynamically.
"""
