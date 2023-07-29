"""
Prototype design pattern:

The Prototype design pattern is a creational design pattern that allows you to create new objects by copying existing objects (prototypes) without making the code dependent on their classes. In other words, it involves cloning objects rather than creating them from scratch. This pattern is useful when the cost of creating a new object is expensive or when the new object is very similar to an existing one.

The Prototype pattern typically involves two main components:

1) Prototype Interface: This is an interface or an abstract class that declares a method for cloning itself.

2) Concrete Prototypes: These are the actual objects that implement the Prototype Interface and provide the cloning functionality.
"""

import copy

# Prototype Interface
class Prototype:
    def clone(self):
        pass

# Concrete Prototype
class Sheep(Prototype):
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def clone(self):
        return copy.copy(self)

    def __str__(self):
        return f"{self.name} ({self.category})"

# Client Code
if __name__ == "__main__":
    original_sheep = Sheep("Dolly", "Merino")
    print("Original Sheep:", original_sheep)

    # Cloning the original sheep to create a new sheep
    cloned_sheep = original_sheep.clone()
    cloned_sheep.name = "Lily"
    print("Cloned Sheep:", cloned_sheep)




"""
In this example, we have a Prototype interface that declares a clone() method. The Sheep class is a concrete prototype that implements the Prototype interface. When we want to create a new Sheep, we simply clone the original sheep using the clone() method, and then modify any unique attributes if needed.

The copy.copy() function is used for shallow copying in Python, which creates a new object with a new reference but does not create new copies of the object's attributes. If you need a deep copy (i.e., new copies of the attributes as well), you can use copy.deepcopy().

The Prototype design pattern is beneficial when there is a need for creating objects with similar properties, and it can help reduce the overhead of object creation. Additionally, it provides a level of abstraction, making the client code independent of the concrete classes used for cloning objects.
"""
