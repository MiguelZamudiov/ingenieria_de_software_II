from payment_factory import PaymentFactory


class App:
    def run(self):
        payment1 = PaymentFactory.create_payment("card")
        payment1.pay(100)

        payment2 = PaymentFactory.create_payment("bank")
        payment2.pay(250)