from fuzzy_expert.rule import FuzzyRule

__rules = [
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

class IsothermalTransformationRulesWrapper:
    def __init__(self):
        self.__fuzzy_rules = __rules

    def getIsothermalTransformationRules(self):
        return self.__fuzzy_rules
    

    
    