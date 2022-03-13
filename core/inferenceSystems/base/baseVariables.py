from abc import abstractmethod, ABC


class BaseVariableWrapper(ABC):

    @abstractmethod
    def set_variables(self): pass

    def __init__(self):
        self._fuzzy_variables = None

    @property
    def variables(self):
        return self._fuzzy_variables
