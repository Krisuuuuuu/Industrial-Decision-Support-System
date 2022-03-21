from fuzzy_expert.variable import FuzzyVariable
import core.inferenceSystems.base.baseVariables as v

AUSTENITIZATION_PROCESS_VARIABLES = {
    "austenitization_process_time": FuzzyVariable(
        universe_range=(0, 24),
        terms={
            "Unsuitable": [(0, 1), (0.45, 1), (0.5, 0), (3.95, 0), (4.0, 1), (24, 1)],
            "Very_Short": ('trapmf', 0.45, 0.5, 0.95, 1.0),
            "Short": ('trapmf', 0.95, 1.0, 1.45, 1.5),
            "Medium": ('trapmf', 1.45, 1.5, 1.95, 2.0),
            "Long": ('trapmf', 1.95, 2, 2.45, 2.5),
            "Very_Long": ('trapmf', 2.45, 2.5, 3.95, 4),
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


class AustenitizationProcessVariableWrapper(v.BaseVariableWrapper):
    def __init__(self):
        global AUSTENITIZATION_PROCESS_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = AUSTENITIZATION_PROCESS_VARIABLES

