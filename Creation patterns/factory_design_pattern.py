"""
Factory method design pattern:


The Factory Method design pattern is a creational pattern that provides an interface for creating objects but allows subclasses to alter the type of objects that will be created. It promotes loose coupling and provides a way to create objects without specifying the exact class of the object that will be created.

Let's create an example of a Document factory, where we have a base class Document and two concrete document classes: PDFDocument and WordDocument. We'll use a factory method to create instances of these classes.
"""

from abc import ABC, abstractmethod

# Product interface
class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass

# Concrete Product class
class PDFDocument(Document):
    def open(self):
        print("Opening PDF document")

    def save(self):
        print("Saving PDF document")

# Concrete Product class
class WordDocument(Document):
    def open(self):
        print("Opening Word document")

    def save(self):
        print("Saving Word document")

# Creator (Factory) class
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass

# Concrete Creator class
class PDFDocumentCreator(DocumentCreator):
    def create_document(self):
        return PDFDocument()

# Concrete Creator class
class WordDocumentCreator(DocumentCreator):
    def create_document(self):
        return WordDocument()

# Example usage
if __name__ == "__main__":
    pdf_creator = PDFDocumentCreator()
    pdf_document = pdf_creator.create_document()
    pdf_document.open()
    pdf_document.save()

    word_creator = WordDocumentCreator()
    word_document = word_creator.create_document()
    word_document.open()
    word_document.save()





"""
In this example, the Document class is the product interface with two abstract methods open() and save(). The concrete product classes PDFDocument and WordDocument inherit from the Document class and implement their specific behavior.

The DocumentCreator class is the factory (creator) interface with the abstract method create_document(). Concrete creator classes PDFDocumentCreator and WordDocumentCreator inherit from the DocumentCreator class and provide their implementation for the create_document() method, returning instances of the corresponding product classes.

The factory method create_document() allows the client code to create a document without specifying the concrete class of the document. This way, we achieve loose coupling, and the client code doesn't need to know the details of how the documents are created.
"""
