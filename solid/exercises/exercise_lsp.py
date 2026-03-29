from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def make_sound(self) -> None:
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass


class Sparrow(Bird, Flyable):
    def make_sound(self) -> None:
        print("Sparrow: Tweet tweet!")

    def fly(self) -> None:
        print("Sparrow: Flap flap... I'm flying!")


class Eagle(Bird, Flyable):
    def make_sound(self) -> None:
        print("Eagle: Screech!")

    def fly(self) -> None:
        print("Eagle: Soaring high in the sky!")


class Ostrich(Bird):
    def make_sound(self) -> None:
        print("Ostrich: Boom boom!")

    def run(self) -> None:
        print("Ostrich: Running at 70 km/h!")


if __name__ == "__main__":
    birds = [Sparrow(), Eagle(), Ostrich()]
    for bird in birds:
        bird.make_sound()