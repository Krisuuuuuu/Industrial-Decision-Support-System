from abc import abstractmethod, ABC


class AbstractFactory(ABC):

    @abstractmethod
    def create(self): pass
