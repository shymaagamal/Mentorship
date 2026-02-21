# extrnal library


class StripePaymentProcessor:
    def makeCharge(self, value_in_cents: int):
        print(f"Processing payment of ${value_in_cents} using Stripe.")