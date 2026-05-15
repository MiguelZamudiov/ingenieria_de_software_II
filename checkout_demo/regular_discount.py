from discount_strategy import DiscountStrategy


class RegularDiscount(DiscountStrategy):
    def calculate(self, subtotal):
        return subtotal * 0.05