from payment_method import PaymentMethod


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Pagando ${amount} con tarjeta de crédito")