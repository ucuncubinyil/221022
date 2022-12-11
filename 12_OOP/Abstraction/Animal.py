from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class

    @abstractmethod
    def drink(self, a):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def sleep(self):
        pass
