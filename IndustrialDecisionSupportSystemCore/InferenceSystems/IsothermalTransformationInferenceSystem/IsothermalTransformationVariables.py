from fuzzy_expert.variable import FuzzyVariable
import IndustrialDecisionSupportSystemCore.InferenceSystems.Base.BaseVariables as v

ISOTHERMAL_TRANSFORMATION_VARIABLES = {
    "isothermal_transformation_temperature": FuzzyVariable(
        universe_range=(0, 1000),
        terms={
            "Unsuitable": [(0, 1), (219, 1), (2.20, 0), (310, 0), (311, 1), (1000, 1)],
            "Optimal": ('trapmf', 220, 220, 240, 240),
            "Correct": ('trapmf', 241, 241, 270, 270),
            "Average": ('trapmf', 271, 271, 310, 310),
        },
    ),
    "austenitizing_temperature": FuzzyVariable(
        universe_range=(0, 2000),
        terms={
            "Unsuitable": [(0, 1), (814, 1), (815, 0), (950, 0), (951, 1), (2000, 1)],
            "Optimal": ('trapmf', 930, 930, 950, 950),
            "Correct": ('trapmf', 900, 900, 929, 929),
            "Average": ('trapmf', 816, 816, 899, 899),
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


class IsothermalTransformationVariableWrapper(v.BaseVariableWrapper):
    def __init__(self):
        global ISOTHERMAL_TRANSFORMATION_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = ISOTHERMAL_TRANSFORMATION_VARIABLES
