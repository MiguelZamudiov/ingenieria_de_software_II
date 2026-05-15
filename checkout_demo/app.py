from checkout_facade import CheckoutFacade


class App:
    def __init__(self):
        self.checkout = CheckoutFacade()

    def run(self):
        self.checkout.process_order("regular", 1000)
        print()
        self.checkout.process_order("vip", 1000)