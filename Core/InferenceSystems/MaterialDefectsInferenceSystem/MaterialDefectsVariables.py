from fuzzy_expert.variable import FuzzyVariable
import Core.InferenceSystems.Base.BaseVariables as v

MATERIAL_DEFECTS_VARIABLES = {
    "quantity": FuzzyVariable(
        universe_range=(0, 20),
        terms={
            "None": ('trimf', 0, 0, 0),
            "Little": ('trapmf', 1, 1, 4, 5),
            "Average": ('trapmf', 4, 5, 7, 8),
            "Many": ('trapmf', 7, 8, 20, 20),
        },
    ),
    "size": FuzzyVariable(
        universe_range=(0, 10),
        terms={
            "None": ('trimf', 0, 0, 0),
            "Small": ('trapmf', 0, 0.1, 0.5, 0.6),
            "Average": ('trapmf', 0.5, 0.6, 1, 1.1),
            "Big": ('trapmf', 1, 1.1, 10, 10),
        },
    ),
    "decision": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unacceptable": ('trapmf', 0, 0, 20, 25),
            "Weak": ('trapmf', 20, 25, 50, 55),
            "Acceptable": ('trapmf', 50, 55, 75, 80),
            "Perfect": ('trapmf', 75, 80, 100, 100),
        },
    ),
}


class MaterialDefectsVariableWrapper(v.BaseVariableWrapper):
    def __init__(self):
        global MATERIAL_DEFECTS_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = MATERIAL_DEFECTS_VARIABLES

