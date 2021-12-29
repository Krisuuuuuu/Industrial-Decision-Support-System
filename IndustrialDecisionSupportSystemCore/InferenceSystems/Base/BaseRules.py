from abc import abstractmethod, ABC


class BaseRulesWrapper(ABC):

    @abstractmethod
    def set_rules(self): pass

    def __init__(self):
        self.__fuzzy_rules = None

    def get_rules(self):
        return self.__fuzzy_rules
