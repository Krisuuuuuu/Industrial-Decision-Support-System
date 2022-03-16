from fuzzy_expert.variable import FuzzyVariable
import core.inferenceSystems.base.baseVariables as v

MATERIAL_DEFECTS_VARIABLES = {
    "isothermal_transformation_time": FuzzyVariable(
        universe_range=(0, 24),
        terms={
            "Unsuitable": [(0, 1), (0.2, 1), (0.25, 0), (2.95, 0), (3.0, 1), (24, 1)],
            "Very_Short": ('trapmf', 0.20, 0.25, 0.45, 0.5),
            "Short": ('trapmf', 0.45, 0.5, 0.95, 1),
            "Medium": ('trapmf', 0.95, 1, 1.45, 1.5),
            "Long": ('trapmf', 1.45, 1.5, 1.95, 2),
            "Very_Long": ('trapmf', 1.95, 2, 2.95, 3),
        },
    ),
    "wall_thickness": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Small": ('trapmf', 0, 1, 12, 13),
            "Medium": ('trapmf', 12, 13, 49, 50),
            "High": ('trapmf', 49, 50, 100, 100),
        },
    ),
    "decision": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": ('trapmf', 0, 0, 33, 36),
            "Average": ('trapmf', 33, 36, 64, 67),
            "Optimal": ('trapmf', 64, 67, 100, 100)
        },
    ),
}


class IsothermalTransformationVariableWrapper(v.BaseVariableWrapper):
    def __init__(self):
        global MATERIAL_DEFECTS_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = MATERIAL_DEFECTS_VARIABLES

