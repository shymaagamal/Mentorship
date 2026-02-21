from paypal import PaypalProcessor
from stripe_adapter import StripeAdapter


if __name__ == "__main__":
    paypal = PaypalProcessor()
    paypal.process_payment(100.0)

    stripe = StripeAdapter()
    stripe.process_payment(100.0)