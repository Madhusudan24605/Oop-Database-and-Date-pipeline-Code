from abc import ABC, abstractmethod

class Animal(ABC):
    __sound: str

    @abstractmethod
    def _init_(self, sound: str) -> None:
        self.__sound = sound

    def makeSound(self) -> None:
        print(self.__sound)


class Dog(Animal):
    def _init_(self):
        super()._init_("Woof")


class Cat(Animal):
    def _init_(self):
        super()._init_("Meow")


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    dog.makeSound()
    cat.makeSound()