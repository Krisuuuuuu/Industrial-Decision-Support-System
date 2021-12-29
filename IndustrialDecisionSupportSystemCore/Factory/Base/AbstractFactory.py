from abc import abstractmethod, ABC
import IndustrialDecisionSupportSystemCore.Builder.Director as d


class AbstractFactory(ABC):
    @abstractmethod
    def create(self): pass

    def __init__(self):
        self._director = d.Director()
