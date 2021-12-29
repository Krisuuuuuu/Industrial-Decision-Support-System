from fuzzy_expert.rule import FuzzyRule
import IndustrialDecisionSupportSystemCore.InferenceSystems.Base.BaseRules as r

ISOTHERMAL_TRANSFORMATION_RULES = [
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Unsuitable"),
            ("AND", "isothermal_transformation_temperature", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Unsuitable"),
            ("AND", "isothermal_transformation_temperature", "Average")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Unsuitable"),
            ("AND", "isothermal_transformation_temperature", "Correct")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Unsuitable"),
            ("AND", "isothermal_transformation_temperature", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Average"),
            ("AND", "isothermal_transformation_temperature", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Average"),
            ("AND", "isothermal_transformation_temperature", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Average"),
            ("AND", "isothermal_transformation_temperature", "Correct")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Average"),
            ("AND", "isothermal_transformation_temperature", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Correct"),
            ("AND", "isothermal_transformation_temperature", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Correct"),
            ("AND", "isothermal_transformation_temperature", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Correct"),
            ("AND", "isothermal_transformation_temperature", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Correct"),
            ("AND", "isothermal_transformation_temperature", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Optimal"),
            ("AND", "isothermal_transformation_temperature", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Optimal"),
            ("AND", "isothermal_transformation_temperature", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Optimal"),
            ("AND", "isothermal_transformation_temperature", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("austenitizing_temperature", "Optimal"),
            ("AND", "isothermal_transformation_temperature", "Optimal")
        ],
        consequence=[("decision", "Optimal")],
    )
]


class IsothermalTransformationRulesWrapper(r.BaseRulesWrapper):
    def __init__(self):
        global ISOTHERMAL_TRANSFORMATION_RULES
        super().__init__()

    def set_rules(self):
        self._fuzzy_rules = ISOTHERMAL_TRANSFORMATION_RULES
