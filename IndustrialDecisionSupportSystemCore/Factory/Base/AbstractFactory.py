from abc import abstractmethod, ABC
from ...Builder.Director import Director


class AbstractFactory(ABC):
    @abstractmethod
    def create(self): pass

    def __init__(self):
        self._director = Director()
