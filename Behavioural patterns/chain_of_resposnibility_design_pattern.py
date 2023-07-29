"""
Chain of Responsibility design pattern:

The Chain of Responsibility design pattern is a behavioral design pattern that allows multiple objects to handle a request without explicitly specifying which object will handle it. The pattern creates a chain of handler objects, where each handler has a reference to the next handler in the chain. When a request is made, it is passed along the chain until a suitable handler is found that can process the request.

Key components of the Chain of Responsibility pattern:

Handler Interface/Abstract Class: This defines the common interface for all handlers in the chain. It usually includes a method to handle the request and a reference to the next handler.

Concrete Handlers: These are the actual handler objects that implement the Handler interface. Each concrete handler decides whether it can handle the request and either processes it or passes it to the next handler in the chain.

Client: The client initiates the request and starts the chain by passing the request to the first handler.

The Chain of Responsibility pattern promotes loose coupling between the sender of a request and its receiver, as the client does not need to know which handler will process the request.
"""

# Handler Interface
class Handler:
    def set_next(self, handler):
        pass

    def handle_request(self, request):
        pass

# Concrete Handlers
class ConcreteHandlerA(Handler):
    def set_next(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if request == "A":
            print("ConcreteHandlerA handles the request.")
        elif self.next_handler:
            self.next_handler.handle_request(request)

class ConcreteHandlerB(Handler):
    def set_next(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if request == "B":
            print("ConcreteHandlerB handles the request.")
        elif self.next_handler:
            self.next_handler.handle_request(request)

class ConcreteHandlerC(Handler):
    def set_next(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if request == "C":
            print("ConcreteHandlerC handles the request.")
        elif self.next_handler:
            self.next_handler.handle_request(request)

# Client
if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConcreteHandlerC()

    handler_a.set_next(handler_b)
    handler_b.set_next(handler_c)

    # Client initiates the request and starts the chain
    handler_a.handle_request("A")  # Output: ConcreteHandlerA handles the request.
    handler_a.handle_request("B")  # Output: ConcreteHandlerB handles the request.
    handler_a.handle_request("C")  # Output: ConcreteHandlerC handles the request.



"""

"""
