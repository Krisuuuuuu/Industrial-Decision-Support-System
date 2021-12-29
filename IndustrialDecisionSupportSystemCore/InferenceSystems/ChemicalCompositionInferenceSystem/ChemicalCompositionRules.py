from fuzzy_expert.rule import FuzzyRule
import IndustrialDecisionSupportSystemCore.InferenceSystems.Base.BaseRules as r

CHEMICAL_COMPOSITION_RULES = [
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),  # 10
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Average")],
    ),  # 20
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),  # 30
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Unsuitable")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Unsuitable"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Optimal")],
    ),  # 40
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),  # 50
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),  # 60
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "silicon", "Correct"),
            ("AND", "manganese", "Correct")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Correct"),
            ("AND", "silicon", "Optimal"),
            ("AND", "manganese", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "silicon", "Average"),
            ("AND", "manganese", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    )
]


class ChemicalCompositionRulesWrapper(r.BaseRulesWrapper):
    def __init__(self):
        global CHEMICAL_COMPOSITION_RULES
        super().__init__()

    def set_rules(self):
        self._fuzzy_rules = CHEMICAL_COMPOSITION_RULES
