
# This is the adapter class that allows us 
# to use the StripePaymentProcessor external library with our existing PaymentProcessor interface
from PaymentProcessor import PaymentProcessor
from stripe_sdk import StripePaymentProcessor

class StripeAdapter(PaymentProcessor):
    def __init__(self):
        self.stripe_processor = StripePaymentProcessor()  

    def process_payment(self, amount: float):
        cents = round(amount * 100)
        self.stripe_processor.makeCharge(int(cents)) # Stripe processes amounts in cents