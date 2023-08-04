# We will create our own types in this module.
from abc import ABC, ABCMeta, abstractmethod


class SomeABC(ABC):
    @abstractmethod
    def some_abstractmethod(self):
        pass

class A(metaclass=ABCMeta):
    pass
