"""
Iterator design pattern:

The Iterator design pattern is a behavioral pattern that provides a way to access elements of a collection sequentially without exposing the underlying representation of the collection. It allows you to traverse the elements of a collection without knowing the internal structure of the collection.
"""

from abc import ABC, abstractmethod

# Iterator interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Concrete Iterator class for list traversal
class ListIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            value = self._collection[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration()

# Aggregate interface
class Aggregate(ABC):
    @abstractmethod
    def get_iterator(self):
        pass

# Concrete Aggregate class for a list
class ListAggregate(Aggregate):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_iterator(self):
        return ListIterator(self._items)

# Client code
if __name__ == "__main__":
    list_aggregate = ListAggregate()
    list_aggregate.add_item("Item 1")
    list_aggregate.add_item("Item 2")
    list_aggregate.add_item("Item 3")

    iterator = list_aggregate.get_iterator()

    while iterator.has_next():
        print(iterator.next())



"""
In this example, we have an Iterator abstract class that defines the common interface for iterating over elements. The ListIterator is a concrete iterator that provides implementation for traversing a list.

The Aggregate abstract class represents the collection, and the ListAggregate is a concrete implementation of the collection using a list.

The client code creates a ListAggregate and adds items to it. It obtains the iterator using get_iterator() and then iterates over the elements using the iterator's has_next() and next() methods.
"""
