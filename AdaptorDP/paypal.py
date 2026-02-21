
# this is the applicaion code which support paypal payment method.
# and we want to add support for stripe payment method without changing the existing code. 
# so we will use adaptor design pattern to achieve this.

from PaymentProcessor import PaymentProcessor


class PaypalProcessor(PaymentProcessor):
  
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} using PayPal.")