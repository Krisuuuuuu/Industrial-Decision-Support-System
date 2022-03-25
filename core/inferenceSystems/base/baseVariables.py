from abc import abstractmethod, ABC

from fuzzy_expert.variable import FuzzyVariable


class BaseVariableWrapper(ABC):

    @abstractmethod
    def set_variables(self) -> None: pass

    def __init__(self):
        self._fuzzy_variables: dict[str, FuzzyVariable] = None

    @property
    def variables(self) -> dict[str, FuzzyVariable]:
        return self._fuzzy_variables
