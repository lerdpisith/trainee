from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass


class VIPDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.8


class StandardDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.9


class NoDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount


class PremiumDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.7


class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, amount: float) -> float:
        return self.strategy.calculate(amount)


if __name__ == "__main__":
    amount = 100
    scenarios = [
        ("VIP",      VIPDiscount()),
        ("Standard", StandardDiscount()),
        ("Normal",   NoDiscount()),
        ("Premium",  PremiumDiscount()),
    ]
    for label, strategy in scenarios:
        calc = DiscountCalculator(strategy)
        print(f"{label:10} price: {calc.calculate(amount):.2f}")