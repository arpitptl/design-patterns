"""
Bridge design pattern:

The Bridge design pattern is a structural pattern that separates the abstraction from its implementation, allowing both to vary independently. It is useful when you have multiple dimensions of variations, and you want to decouple the abstraction and implementation hierarchies.

Let's create an example of a Bridge pattern for a drawing application. We'll have a Shape abstraction with two concrete implementations: CircleShape and SquareShape. We'll also have a Renderer interface with two concrete implementations: VectorRenderer and RasterRenderer. The Bridge pattern allows us to draw different shapes using different rendering methods.
"""

from abc import ABC, abstractmethod

# Abstraction - Shape
class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

# Concrete Abstraction - CircleShape
class CircleShape(Shape):
    def draw(self):
        print("Drawing a circle.")
        self.renderer.render_circle()

# Concrete Abstraction - SquareShape
class SquareShape(Shape):
    def draw(self):
        print("Drawing a square.")
        self.renderer.render_square()

# Implementor - Renderer
class Renderer(ABC):
    @abstractmethod
    def render_circle(self):
        pass

    @abstractmethod
    def render_square(self):
        pass

# Concrete Implementor - VectorRenderer
class VectorRenderer(Renderer):
    def render_circle(self):
        print("Rendering a circle in vector format.")

    def render_square(self):
        print("Rendering a square in vector format.")

# Concrete Implementor - RasterRenderer
class RasterRenderer(Renderer):
    def render_circle(self):
        print("Rendering a circle in raster format.")

    def render_square(self):
        print("Rendering a square in raster format.")

# Example usage
if __name__ == "__main__":
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle = CircleShape(vector_renderer)
    circle.draw()
    # Output: Drawing a circle.
    #         Rendering a circle in vector format.

    square = SquareShape(raster_renderer)
    square.draw()
    # Output: Drawing a square.
    #         Rendering a square in raster format.






"""
In this example, the Shape class is the abstraction, and the Renderer class is the implementor. The Shape class has a reference to the Renderer object and uses it to render the shape.

The concrete shape classes (CircleShape and SquareShape) inherit from Shape and implement the draw() method. They call the corresponding rendering methods provided by the Renderer object, allowing the shapes to be drawn using different rendering methods.

The concrete renderer classes (VectorRenderer and RasterRenderer) inherit from Renderer and implement the rendering methods for circles and squares in different formats.

By using the Bridge pattern, we separate the shape hierarchy from the renderer hierarchy, allowing both to vary independently. This makes it easy to add new shapes or renderers without modifying existing classes, promoting flexibility and extensibility in the drawing application.
"""
