from discount_factory import DiscountFactory


class CheckoutFacade:
    def process_order(self, customer_type, subtotal):
        strategy = DiscountFactory.get_strategy(customer_type)
        discount = strategy.calculate(subtotal)
        total = subtotal - discount

        print(f"Cliente: {customer_type}")
        print(f"Subtotal: ${subtotal}")
        print(f"Descuento: ${discount}")
        print(f"Total a pagar: ${total}")