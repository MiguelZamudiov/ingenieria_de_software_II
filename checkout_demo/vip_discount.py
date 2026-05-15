from discount_strategy import DiscountStrategy


class VIPDiscount(DiscountStrategy):
    def calculate(self, subtotal):
        return subtotal * 0.15