"""
Strategy design pattern:

The Strategy design pattern allows you to define a family of algorithms (strategies) and make them interchangeable within a context without altering the client code. It promotes flexibility and maintainability by encapsulating each algorithm as a separate class and enabling dynamic selection of the desired strategy.

Let's see a simple example of the Strategy design pattern in Python. We'll implement a payment system that supports different payment methods: CreditCardPayment and PayPalPayment.
"""


from abc import ABC, abstractmethod

# Abstract PaymentStrategy class (Strategy interface)
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete strategy class for Credit Card payment
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paying ${amount} with Credit Card: {self.card_number}")

# Concrete strategy class for PayPal payment
class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        print(f"Paying ${amount} with PayPal: {self.email}")

# Context class
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def calculate_total(self):
        # Assume some logic to calculate the total amount in the shopping cart
        return 100  # Sample total amount

    def checkout(self):
        total_amount = self.calculate_total()
        self.payment_strategy.pay(total_amount)

# Example usage
if __name__ == "__main__":
    credit_card_payment = CreditCardPayment("1234 5678 9012 3456", "12/25", "123")
    paypal_payment = PayPalPayment("example@example.com", "password")

    cart1 = ShoppingCart(credit_card_payment)
    cart2 = ShoppingCart(paypal_payment)

    cart1.checkout()  # Output: Paying $100 with Credit Card: 1234 5678 9012 3456
    cart2.checkout()  # Output: Paying $100 with PayPal: example@example.com




"""
In this example, we have an abstract PaymentStrategy class, which serves as the Strategy interface, defining a common method pay(). Concrete payment methods (CreditCardPayment and PayPalPayment) implement the pay() method with their specific payment logic.

The ShoppingCart class serves as the context that uses a payment strategy during the checkout process. The client code can create instances of the ShoppingCart and provide different payment strategies based on the desired payment method.

By using the Strategy pattern, we can easily add new payment methods without modifying the existing code. It allows for a more maintainable and flexible design, making it easier to extend and modify the payment system.
"""