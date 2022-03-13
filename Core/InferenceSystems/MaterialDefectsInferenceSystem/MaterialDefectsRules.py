from fuzzy_expert.rule import FuzzyRule
import Core.InferenceSystems.Base.BaseRules as r

MATERIAL_DEFECTS_RULES = [
    FuzzyRule(
        premise=[
            ("quantity", "None"),
            ("AND", "size", "None"),
        ],
        consequence=[("decision", "Perfect")],
    ),
    FuzzyRule(
        premise=[
            ("quantity", "Little"),
            ("AND", "size", "Small"),
        ],
        consequence=[("decision", "Acceptable")],
    ),
    FuzzyRule(
        premise=[
            ("quantity", "Little"),
            ("AND", "size", "Average"),
        ],
        consequence=[("decision", "Weak")],
    ),
    FuzzyRule(
        premise=[
            ("quantity", "Little"),
            ("AND", "size", "Big"),
        ],
        consequence=[("decision", "Unacceptable")],
    ),
    FuzzyRule(
        premise=[
            ("quantity", "Average"),
            ("AND", "size", "Small"),
        ],
        consequence=[("decision", "Weak")],
    ),
    FuzzyRule(
        premise=[
            ("quantity", "Average"),
            ("AND", "size", "Average"),
        ],
        consequence=[("decision", "Unacceptable")],
    ),
    FuzzyRule(
        premise=[
            ("quantity", "Average"),
            ("AND", "size", "Big"),
        ],
        consequence=[("decision", "Unacceptable")],
    ),
    FuzzyRule(
        premise=[
            ("quantity", "Many"),
            ("AND", "size", "Small"),
        ],
        consequence=[("decision", "Unacceptable")],
    ),
    FuzzyRule(
        premise=[
            ("quantity", "Many"),
            ("AND", "size", "Average"),
        ],
        consequence=[("decision", "Unacceptable")],
    ),
    FuzzyRule(
        premise=[
            ("quantity", "Many"),
            ("AND", "size", "Big"),
        ],
        consequence=[("decision", "Unacceptable")],
    ),
]


class MaterialDefectsRulesWrapper(r.BaseRulesWrapper):
    def __init__(self):
        global MATERIAL_DEFECTS_RULES
        super().__init__()

    def set_rules(self):
        self._fuzzy_rules = MATERIAL_DEFECTS_RULES
