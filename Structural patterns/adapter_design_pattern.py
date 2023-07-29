"""
Adapter design pattern:

The Adapter design pattern allows incompatible interfaces of different classes to work together. It acts as a bridge between two interfaces, converting the interface of one class into another interface that the client expects.

Let's create an example of an adapter design pattern for a payment gateway system. We have an existing PaymentGateway class with its interface, and we want to use a third-party payment gateway ThirdPartyPaymentGateway that has a different interface. We'll create an adapter class, ThirdPartyPaymentAdapter, to make the ThirdPartyPaymentGateway compatible with our existing system.
"""

# Existing PaymentGateway class with its interface
class PaymentGateway:
    def process_payment(self, amount):
        raise NotImplementedError("process_payment method not implemented in PaymentGateway.")

# Third-party payment gateway with a different interface
class ThirdPartyPaymentGateway:
    def perform_payment(self, total_amount):
        print(f"Processing payment for ${total_amount} through ThirdPartyPaymentGateway.")

# Adapter class to make ThirdPartyPaymentGateway compatible with PaymentGateway
class ThirdPartyPaymentAdapter(PaymentGateway):
    def __init__(self, third_party_gateway):
        self.third_party_gateway = third_party_gateway

    def process_payment(self, amount):
        self.third_party_gateway.perform_payment(amount)

# Client code that expects PaymentGateway interface
def make_payment(payment_gateway, amount):
    payment_gateway.process_payment(amount)

# Example usage
if __name__ == "__main__":
    payment_gateway = PaymentGateway()
    make_payment(payment_gateway, 100)  # Output: NotImplementedError

    third_party_gateway = ThirdPartyPaymentGateway()
    third_party_adapter = ThirdPartyPaymentAdapter(third_party_gateway)
    make_payment(third_party_adapter, 150)  # Output: Processing payment for $150 through ThirdPartyPaymentGateway.





"""
In this example, we have the existing PaymentGateway class with its process_payment() method. We also have a third-party payment gateway ThirdPartyPaymentGateway with a perform_payment() method.

The ThirdPartyPaymentAdapter class acts as an adapter, inheriting from PaymentGateway and containing an instance of ThirdPartyPaymentGateway. It implements the process_payment() method by invoking the perform_payment() method of the third-party payment gateway, making it compatible with our existing system.

The make_payment() function is the client code that expects the PaymentGateway interface. When we pass an instance of PaymentGateway, it raises a NotImplementedError, but when we pass an instance of ThirdPartyPaymentAdapter, it calls the adapted method and processes the payment through the third-party payment gateway.

By using the Adapter design pattern, we can integrate third-party components or libraries with our existing system without modifying the original code, promoting code reusability and flexibility.
"""
