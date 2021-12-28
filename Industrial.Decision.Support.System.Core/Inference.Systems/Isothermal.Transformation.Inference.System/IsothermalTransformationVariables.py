from fuzzy_expert.variable import FuzzyVariable
from ..Base.BaseVariables import BaseVariableWrapper

__isothermalTransformationVariables = {
    "isothermal_transformation_temperature": FuzzyVariable(
        universe_range=(0, 1000),
        terms={
            "Unsuitable": ('trapmf', 0, 0, 220, 220),
            "Optimal": ('trapmf', 220, 220, 240, 240),
            "Correct": ('trapmf', 241, 241, 270, 270),
            "Average": ('trapmf', 271, 271, 310, 310),
            "Unsuitable": ('trapmf', 311, 311, 1000, 1000),
        },
    ),
    "austenitizing_temperature": FuzzyVariable(
        universe_range=(0, 2000),
        terms={
            "Unsuitable": ('trapmf', 0, 0, 815, 815),
            "Optimal": ('trapmf', 930, 930, 950, 950),
            "Correct": ('trapmf', 900, 900, 929, 929),
            "Average": ('trapmf', 816, 816, 899, 899),
            "Unsuitable": ('trapmf', 951, 951, 2000, 2000),
        },
    )
}

class IsothermalTransformationVariableWrapper:
    def setVariables(self):
        self.__fuzzy_variables = __isothermalTransformationVariables




