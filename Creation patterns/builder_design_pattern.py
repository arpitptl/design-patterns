"""
Builder design pattern:

The Builder design pattern is a creational pattern that separates the construction of a complex object from its representation. It allows you to create different representations of an object while using the same construction code. This pattern is useful when you have a complex object with many optional parameters or configurations.
"""

class Pizza:
    def __init__(self):
        self.size = ""
        self.crust = ""
        self.toppings = []

    def __str__(self):
        return f"Size: {self.size}, Crust: {self.crust}, Toppings: {', '.join(self.toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_crust(self, crust):
        self.pizza.crust = crust
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        return self.pizza


# Director (Optional)
class Waiter:
    def __init__(self, pizza_builder):
        self.pizza_builder = pizza_builder

    def construct_pizza(self, size, crust, toppings):
        return self.pizza_builder \
            .set_size(size) \
            .set_crust(crust) \
            .add_topping(toppings) \
            .build()


# Example usage:
if __name__ == "__main__":
    pizza_builder = PizzaBuilder()

    # Using the builder to create different pizza configurations
    pizza1 = pizza_builder.set_size("Medium").set_crust("Thin").add_topping("Cheese").add_topping("Mushrooms").build()
    pizza2 = pizza_builder.set_size("Large").set_crust("Thick").add_topping("Pepperoni").add_topping("Olives").build()

    print("Pizza 1:", pizza1)
    print("Pizza 2:", pizza2)

    # Using Director (Waiter) to create a pizza
    waiter = Waiter(pizza_builder)
    pizza3 = waiter.construct_pizza("Small", "Regular", ["Onions", "Bell Peppers", "Sausage"])
    print("Pizza 3:", pizza3)




"""
In this example, we have a Pizza class representing the complex object we want to build. The PizzaBuilder class handles the construction process by setting the size, crust, and toppings one by one. The build() method returns the final constructed Pizza object.

Using the builder, we can create different pizza configurations without directly dealing with the complexities of the Pizza object's construction. Additionally, we have an optional Waiter class acting as a director, which simplifies the process of constructing a pizza by using the PizzaBuilder.

This way, the Builder design pattern allows for flexible and more readable code when creating complex objects with many optional parameters or configurations.

"""
