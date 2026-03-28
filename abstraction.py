from abc import ABC, abstractmethod


class Airplane(ABC):
    def __init__(self, flight_number: str, route: str):
        self.flight_number = flight_number
        self.route = route

    @abstractmethod
    def fly(self):
        # บังคับให้คลาสลูกต้องมี Method fly()
        pass

class Airbus(Airplane):
    def fly(self):
        print(f"Airbus {self.flight_number} is flying to {self.route}")

class Boeing(Airplane):
    def fly(self):
        print(f"Boeing {self.flight_number} is flying to {self.route}")

if __name__ == '__main__':
    airbus = Airbus("A320", "Phuket")
    airbus.fly()

    boeing = Boeing("B777", "Seoul")
    boeing.fly()