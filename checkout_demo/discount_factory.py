from regular_discount import RegularDiscount
from vip_discount import VIPDiscount


class DiscountFactory:
    @staticmethod
    def get_strategy(customer_type):
        if customer_type == "regular":
            return RegularDiscount()
        elif customer_type == "vip":
            return VIPDiscount()
        else:
            raise ValueError("Tipo de cliente no válido")