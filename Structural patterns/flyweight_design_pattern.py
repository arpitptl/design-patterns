"""
Flyweight design pattern:

The Flyweight design pattern is a structural design pattern that aims to minimize memory usage and improve performance by sharing data among multiple similar objects. It is useful when you need to create a large number of objects with similar attributes and behaviors, and the duplication of data across these objects would lead to excessive memory consumption.

The Flyweight pattern achieves this by separating intrinsic (shared) and extrinsic (unique) states of objects. Intrinsic state refers to the properties that are common and can be shared among multiple objects, while extrinsic state refers to the properties that are specific and vary for each object. By sharing the intrinsic state and storing the extrinsic state externally, the pattern ensures that only one instance of each unique intrinsic state exists in memory.

Key components of the Flyweight pattern:

Flyweight: This is the interface or abstract class that declares methods that the concrete flyweights must implement. The flyweights represent the shared intrinsic state.

Concrete Flyweight: These are the concrete implementations of the Flyweight interface. They represent the shared intrinsic state and must be made immutable.

Flyweight Factory: This is a factory that manages the creation and sharing of flyweight objects. It ensures that only one instance of each unique intrinsic state is created and reused.

Client: The client code creates and uses flyweight objects. The client can pass extrinsic state to the flyweights when needed.


"""

import random
import string

# Flyweight Interface
class Circle:
    def draw(self, x, y):
        pass

# Concrete Flyweight
class ColoredCircle(Circle):
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):
        print(f"Drawing a {self.color} circle at ({x}, {y})")

# Flyweight Factory
class CircleFactory:
    _circle_pool = {}

    @staticmethod
    def get_circle(color):
        if color not in CircleFactory._circle_pool:
            CircleFactory._circle_pool[color] = ColoredCircle(color)
        return CircleFactory._circle_pool[color]

# Client
class CircleRenderer:
    def __init__(self):
        self.circles = []

    def add_circle(self, color, x, y):
        circle = CircleFactory.get_circle(color)
        circle.draw(x, y)
        self.circles.append(circle)

# Helper function to generate random colors
def generate_random_color():
    colors = ['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White']
    return random.choice(colors)

# Example usage:
if __name__ == "__main__":
    circle_renderer = CircleRenderer()

    # Drawing circles of different colors at random positions
    for _ in range(10):
        color = generate_random_color()
        x, y = random.randint(1, 100), random.randint(1, 100)
        circle_renderer.add_circle(color, x, y)





"""
In this example, we have a Circle interface representing the flyweights, and a ColoredCircle class implementing the interface with intrinsic state (color). The CircleFactory is responsible for managing the creation and sharing of the flyweight objects (colored circles). The CircleRenderer class acts as the client that uses the flyweights to draw circles with different colors at specified positions.

When we create a circle using the CircleFactory, it checks if a circle of the specified color already exists in the _circle_pool. If it exists, it returns the existing instance; otherwise, it creates a new instance and adds it to the pool for future reuse. This way, we ensure that circles with the same color are shared and reused, saving memory and improving performance when dealing with a large number of circles with various colors.

"""
