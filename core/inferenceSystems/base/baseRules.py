from abc import abstractmethod, ABC

from fuzzy_expert.rule import FuzzyRule


class BaseRulesWrapper(ABC):

    @abstractmethod
    def set_rules(self) -> None: pass

    def __init__(self):
        self._fuzzy_rules: list[FuzzyRule] = None

    @property
    def rules(self) -> list[FuzzyRule]:
        return self._fuzzy_rules
