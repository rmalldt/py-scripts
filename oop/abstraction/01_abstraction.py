from abc import ABC, abstractmethod


# Abstract base class for payment providers
class PaymentProvider(ABC):
    @abstractmethod
    def process_payment(self, customer_id: str, amount: float) -> str:
        pass


# Paypal implementation
class Paypal(PaymentProvider):
    def process_payment(self, customer_id: str, amount: float) -> str:
        return (
            f"Processed payment of ${amount:.2f} for customer {customer_id} via PayPal"
        )


# Stripe implementation
class Stripe(PaymentProvider):
    def process_payment(self, customer_id: str, amount: float) -> str:
        return (
            f"Processed payment of ${amount:.2f} for customer {customer_id} via Stripe"
        )


# Customer class
class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name

    # `make_payment` does not need to know anything about the PaymentProvider implementation
    def make_payment(self, provider: PaymentProvider, amount: float):
        print(provider.process_payment(self.customer_id, amount))


# Main function
def main() -> None:
    # Create customers
    customer1 = Customer("C123", "Jim")
    customer2 = Customer("C456", "Kale")

    # Create payment providers
    paypal = Paypal()
    stripe = Stripe()

    # Customers make payments
    customer1.make_payment(paypal, 100.0)
    customer2.make_payment(stripe, 200.0)


if __name__ == "__main__":
    main()
