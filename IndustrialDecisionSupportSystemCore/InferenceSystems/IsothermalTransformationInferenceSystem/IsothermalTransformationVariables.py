from fuzzy_expert.variable import FuzzyVariable
import IndustrialDecisionSupportSystemCore.InferenceSystems.Base.BaseVariables as v

MATERIAL_DEFECTS_VARIABLES = {
    "isothermal_transformation_temperature": FuzzyVariable(
        universe_range=(0, 1000),
        terms={
            "Unsuitable": [(0, 1), (215, 1), (2.20, 0), (310, 0), (315, 1), (1000, 1)],
            "Optimal": ('trapmf', 215, 220, 235, 240),
            "Correct": ('trapmf', 235, 240, 265, 270),
            "Average": ('trapmf', 265, 270, 310, 315),
        },
    ),
    "austenitizing_temperature": FuzzyVariable(
        universe_range=(0, 1000),
        terms={
            "Unsuitable": [(0, 1), (810, 1), (815, 0), (945, 0), (950, 1), (1000, 1)],
            "Optimal": ('trapmf', 925, 930, 945, 950),
            "Correct": ('trapmf', 895, 900, 925, 930),
            "Average": ('trapmf', 810, 815, 895, 900),
        },
    ),
    "decision": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": ('trapmf', 0, 0, 20, 25),
            "Average": ('trapmf', 20, 25, 50, 55),
            "Correct": ('trapmf', 50, 55, 75, 80),
            "Optimal": ('trapmf', 75, 80, 100, 100),
        },
    ),
}


class IsothermalTransformationVariableWrapper(v.BaseVariableWrapper):
    def __init__(self):
        global MATERIAL_DEFECTS_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = MATERIAL_DEFECTS_VARIABLES

