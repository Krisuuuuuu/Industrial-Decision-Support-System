from abc import abstractmethod, ABC
import core.builder.director as d


class AbstractFactory(ABC):
    @abstractmethod
    def create(self): pass

    def __init__(self, model):
        self._director = d.Director()
        self._model = model
