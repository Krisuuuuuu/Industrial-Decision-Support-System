from fuzzy_expert.rule import FuzzyRule

from core.inferenceSystems.base.baseRules import BaseRulesWrapper

CHEMICAL_COMPOSITION_RULES = []


class ChemicalCompositionRulesWrapper(BaseRulesWrapper):
    def __init__(self):
        global CHEMICAL_COMPOSITION_RULES
        super().__init__()

    def set_rules(self):
        self._fuzzy_rules = CHEMICAL_COMPOSITION_RULES
