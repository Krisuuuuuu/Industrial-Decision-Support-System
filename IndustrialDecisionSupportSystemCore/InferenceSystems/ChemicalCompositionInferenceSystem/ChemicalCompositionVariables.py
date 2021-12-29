from fuzzy_expert.variable import FuzzyVariable
import IndustrialDecisionSupportSystemCore.InferenceSystems.Base.BaseVariables as v

CHEMICAL_COMPOSITION_VARIABLES = {
    "carbon": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": [(0, 1), (3.39, 1), (3.40, 0), (3.80, 0), (3.81, 1), (100, 1)],
            "Average": ('trapmf', 3.40, 3.40, 3.59, 3.59),
            "Correct": ('trapmf', 3.61, 3.61, 3.80, 3.80),
            "Optimal": ('trimf', 3.60, 3.60, 3.60),
        },
    ),
    "silicon": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": [(0, 1), (2.29, 1), (2.30, 0), (2.70, 0), (2.71, 1), (100, 1)],
            "Average": ('trapmf', 2.30, 2.30, 2.49, 2.49),
            "Correct": ('trapmf', 2.51, 2.51, 2.70, 2.70),
            "Optimal": ('trimf', 2.50, 2.50, 2.50),
        },
    ),
    "manganese": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": [(0, 1), (0.29, 1), (0.30, 0), (0.40, 0), (0.41, 1), (100, 1)],
            "Average": [(0.29, 0), (0.30, 1), (0.32, 1), (0.33, 0), (0.37, 0), (0.38, 1), (0.40, 1), (0.41, 0)],
            "Correct": [(0.32, 0), (0.33, 1), (0.34, 1), (0.35, 0), (0.36, 1), (0.37, 1), (0.38, 0)],
            "Optimal": ('trimf', 0.35, 0.35, 0.35),
        },
    ),
    "decision": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": ('trapmf', 0, 0, 25, 25),
            "Optimal": ('trapmf', 26, 26, 50, 50),
            "Correct": ('trapmf', 51, 51, 75, 75),
            "Average": ('trapmf', 76, 76, 100, 100),
        },
    ),
}


class ChemicalCompositionVariableWrapper(v.BaseVariableWrapper):
    def __init__(self):
        global CHEMICAL_COMPOSITION_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = CHEMICAL_COMPOSITION_VARIABLES
