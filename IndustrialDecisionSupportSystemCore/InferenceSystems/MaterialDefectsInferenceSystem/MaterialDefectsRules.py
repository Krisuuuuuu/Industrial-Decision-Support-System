from fuzzy_expert.rule import FuzzyRule
import IndustrialDecisionSupportSystemCore.InferenceSystems.Base.BaseRules as r

MATERIAL_DEFECTS_RULES = []


class MaterialDefectsRulesWrapper(r.BaseRulesWrapper):
    def __init__(self):
        global MATERIAL_DEFECTS_RULES
        super().__init__()

    def set_rules(self):
        self._fuzzy_rules = MATERIAL_DEFECTS_RULES
