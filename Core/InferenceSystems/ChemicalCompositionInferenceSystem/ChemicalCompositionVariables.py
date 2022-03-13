from fuzzy_expert.variable import FuzzyVariable
import Core.InferenceSystems.Base.BaseVariables as v

CHEMICAL_COMPOSITION_VARIABLES = {
    "carbon": FuzzyVariable(
        universe_range=(0, 10),
        terms={
            "Unsuitable": [(0, 1), (3.38, 1), (3.40, 0), (3.78, 0), (3.80, 1), (100, 1)],
            "Average": ('trapmf', 3.38, 3.40, 3.58, 3.60),
            "Correct": ('trapmf', 3.60, 3.62, 3.78, 3.80),
            "Optimal": ('trimf', 3.60, 3.60, 3.60),
        },
    ),
    "silicon": FuzzyVariable(
        universe_range=(0, 10),
        terms={
            "Unsuitable": [(0, 1), (2.28, 1), (2.30, 0), (2.68, 0), (2.70, 1), (100, 1)],
            "Average": ('trapmf', 2.28, 2.30, 2.48, 2.50),
            "Correct": ('trapmf', 2.48, 2.50, 2.68, 2.70),
            "Optimal": ('trimf', 2.50, 2.50, 2.50),
        },
    ),
    "manganese": FuzzyVariable(
        universe_range=(0, 10),
        terms={
            "Unsuitable": [(0, 1), (0.29, 1), (0.30, 0), (0.39, 0), (0.40, 1), (100, 1)],
            "Average": [(0.29, 0), (0.30, 1), (0.32, 1), (0.33, 0), (0.37, 0), (0.38, 1), (0.39, 1), (0.40, 0)],
            "Correct": [(0.32, 0), (0.33, 1), (0.34, 1), (0.35, 0), (0.36, 1), (0.37, 1), (0.38, 0)],
            "Optimal": ('trimf', 0.35, 0.35, 0.35),
        },
    ),
    "decision": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": ('trapmf', 0, 0, 20, 25),
            "Average": ('trapmf', 20, 25, 45, 50),
            "Correct": ('trapmf', 50, 55, 75, 80),
            "Optimal": ('trapmf', 75, 80, 100, 100),
        },
    ),
}


class ChemicalCompositionVariableWrapper(v.BaseVariableWrapper):
    def __init__(self):
        global CHEMICAL_COMPOSITION_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = CHEMICAL_COMPOSITION_VARIABLES
