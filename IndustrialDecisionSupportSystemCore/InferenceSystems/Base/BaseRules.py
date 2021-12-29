class BaseRulesWrapper:
    def __init__(self):
        self.__fuzzy_rules = None

    def set_rules(self): pass

    def get_rules(self):
        return self.__fuzzy_rules
