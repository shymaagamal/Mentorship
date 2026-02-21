# Payment Processing System
The system is designed to support multiple payment gateways without modifying existing code, using the Adapter Design Pattern.

Currently, it supports:
* PayPal (native implementation)
* Stripe (via Adapter)
```
+----------------+        +------------------------+
| PaymentProcessor|<-------| StripeAdapter         |
+----------------+        +------------------------+
| process_payment()|       | process_payment()     |
+----------------+        +------------------------+
                             |
                             v
                     +------------------------+
                     | StripePaymentProcessor |
                     +------------------------+
                     | makeCharge(value_in_cents)|
                     +------------------------+

```      

* PaymentProcessor – Abstract interface that defines process_payment(amount).

* StripePaymentProcessor – External library that expects amounts in cents via makeCharge().

* StripeAdapter – Converts dollars to cents and delegates payment to StripePaymentProcessor.

* PaypalProcessor – Native implementation already conforms to PaymentProcessor.