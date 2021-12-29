from fuzzy_expert.variable import FuzzyVariable
from ..Base.BaseVariables import BaseVariableWrapper

CHEMICAL_COMPOSITION_VARIABLES = {
    "carbon": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": ('trapmf', 0, 0, 3.39, 3.39),
            "Unsuitable": ('trapmf', 3.81, 3.81, 100, 100),
            "Average": ('trapmf', 3.40, 3.40, 3.59, 3.59),
            "Correct": ('trapmf', 3.61, 3.61, 3.80, 3.80),
            "Optimal": ('trimf', 3.60, 3.60, 3.60),
        },
    ),
    "silicon": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": ('trapmf', 0, 0, 2.29, 2.29),
            "Unsuitable": ('trapmf', 2.71, 2.71, 100, 100),
            "Average": ('trapmf', 2.30, 2.30, 2.49, 2.49),
            "Correct": ('trapmf', 2.51, 2.51, 2.70, 2.70),
            "Optimal": ('trimf', 2.50, 2.50, 2.50),
        },
    ),
    "manganese": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": ('trapmf', 0, 0, 0.29, 0.29),
            "Unsuitable": ('trapmf', 0.41, 0.41, 100, 100),
            "Average": ('trapmf', 0.30, 0.30, 0.32, 0.32),
            "Average": ('trapmf', 0.38, 0.38, 0.40, 0.40),
            "Correct": ('trapmf', 0.33, 0.33, 0.34, 0.34),
            "Correct": ('trapmf', 0.36, 0.36, 0.37, 0.37),
            "Optimal": ('trimf', 0.35, 0.35, 0.35),
        },
    ),
}


class ChemicalCompositionVariableWrapper(BaseVariableWrapper):
    def __init__(self):
        global CHEMICAL_COMPOSITION_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = CHEMICAL_COMPOSITION_VARIABLES
