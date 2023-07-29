"""
Singleton design pattern:

The Singleton design pattern ensures that a class has only one instance and provides a global point of access to that instance. It is commonly used when you want to control access to shared resources or want to ensure that only one object of a particular class exists throughout the program.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Example usage
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)  # Output: True





"""
In this example, the Singleton class defines a private class variable _instance, which will hold the single instance of the class. The __new__() method is overridden to ensure that only one instance is created. If the _instance variable is None, it creates a new instance using the super() method and assigns it to the _instance variable. Subsequent calls to create an instance will return the existing instance, ensuring that only one instance of the class exists.

Now, both singleton1 and singleton2 refer to the same instance of the Singleton class, and singleton1 is singleton2 evaluates to True.

Note that while the Singleton pattern has its uses, it is also considered an anti-pattern in some cases, as it can lead to tight coupling and can make testing more challenging. Therefore, it's essential to carefully consider whether the Singleton pattern is the best solution for your specific use case.
"""
