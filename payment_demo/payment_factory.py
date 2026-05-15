from credit_card import CreditCardPayment
from legacy_bank import LegacyBankSystem
from bank_adapter import BankAdapter


class PaymentFactory:
    @staticmethod
    def create_payment(method):
        if method == "card":
            return CreditCardPayment()
        elif method == "bank":
            return BankAdapter(LegacyBankSystem())
        else:
            raise ValueError("Método de pago no válido")