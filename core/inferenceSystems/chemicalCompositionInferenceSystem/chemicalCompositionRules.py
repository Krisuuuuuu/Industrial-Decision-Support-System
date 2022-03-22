from fuzzy_expert.rule import FuzzyRule

from core.inferenceSystems.base.baseRules import BaseRulesWrapper

CHEMICAL_COMPOSITION_RULES = [
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    # 10
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    # 20
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Unsuitable"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    # 30
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    # 40
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    # 50
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Average"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Average")],
    ),
    # 60
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Unsuitable"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Correct")],
    ),
    # 70
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Average"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Unsuitable"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Average"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Unsuitable")
        ],
        consequence=[("decision", "Correct")],
    ),
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Average")
        ],
        consequence=[("decision", "Optimal")],
    ),
    # 80
    FuzzyRule(
        premise=[
            ("carbon", "Optimal"),
            ("AND", "sulfur", "Optimal"),
            ("AND", "magnesium", "Optimal"),
            ("AND", "silicon", "Optimal")
        ],
        consequence=[("decision", "Optimal")],
    ),
]


class ChemicalCompositionRulesWrapper(BaseRulesWrapper):
    def __init__(self):
        global CHEMICAL_COMPOSITION_RULES
        super().__init__()

    def set_rules(self):
        self._fuzzy_rules = CHEMICAL_COMPOSITION_RULES
