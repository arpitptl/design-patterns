"""
Composite design pattern:

The Composite design pattern is a structural pattern that allows you to treat individual objects and compositions of objects uniformly. It composes objects into tree-like structures to represent part-whole hierarchies. With the Composite pattern, clients can use individual objects and compositions of objects in a consistent manner, without distinguishing between them.

The key participants in the Composite pattern are:

Component: It is the base interface or abstract class that declares the common interface for both leaf and composite objects. It defines operations that are applicable to both individual objects and compositions.

Leaf: It represents individual objects in the composition. It implements the Component interface.

Composite: It is a higher-level component that represents compositions of objects. It contains a collection of child components and implements the Component interface. It can also provide additional operations specific to compositions.

The Composite pattern is useful in scenarios where you need to represent part-whole hierarchies and want to treat both individual objects and compositions uniformly. It simplifies the client code and promotes code reusability by allowing you to build complex structures from simple building blocks.

A common example of the Composite pattern is a file system. In a file system, directories can contain files and subdirectories, which can, in turn, contain more files and subdirectories. The individual files and directories (leaf components) and the directories containing files and subdirectories (composite components) are all treated uniformly through the Component interface. This allows clients to perform operations on both individual files and entire directory structures without distinguishing between them.
"""

from abc import ABC, abstractmethod

# Component interface
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf class representing a File
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")

# Composite class representing a Directory
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()

# Client code
if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt")
    file2 = File("file2.txt")

    # Create directories
    sub_directory = Directory("Subdirectory")
    sub_directory.add(file1)
    sub_directory.add(file2)

    root_directory = Directory("Root")
    root_directory.add(file1)
    root_directory.add(file2)
    root_directory.add(sub_directory)

    # Display file system structure
    root_directory.display()





"""
In this example, we have a FileSystemComponent abstract base class (component interface) that declares the common interface for both files and directories. The File class represents the leaf component (individual file), and the Directory class represents the composite component (directory that can contain files and subdirectories).

The Directory class has methods to add and remove components (files or subdirectories). The display() method is overridden to display the file system structure, showing the names of files and directories.

In the client code, we create files (file1 and file2) and directories (sub_directory and root_directory) and add the files to the directories. The display() method of the root_directory is called to display the entire file system structure.

Directory: Root
File: file1.txt
File: file2.txt
Directory: Subdirectory
File: file1.txt
File: file2.txt

"""
