from abc import ABC, abstractmethod


class Base(ABC):

    def __init__(self):
        self.id = str()
        self.name = str()

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
