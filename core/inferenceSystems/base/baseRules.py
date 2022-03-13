from abc import abstractmethod, ABC


class BaseRulesWrapper(ABC):

    @abstractmethod
    def set_rules(self): pass

    def __init__(self):
        self._fuzzy_rules = None

    @property
    def rules(self):
        return self._fuzzy_rules
