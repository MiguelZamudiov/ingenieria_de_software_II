from payment_method import PaymentMethod


class BankAdapter(PaymentMethod):
    def __init__(self, legacy_bank):
        self.legacy_bank = legacy_bank

    def pay(self, amount):
        cents = int(amount * 100)
        self.legacy_bank.make_payment(cents)