from fuzzy_expert.rule import FuzzyRule

__rules = []

class ChemicalCompositionRulesWrapper:
    def __init__(self):
        self.__fuzzy_rules = __rules

    def getChemicalCompositionRules(self):
        return self.__fuzzy_rules
    

    
    