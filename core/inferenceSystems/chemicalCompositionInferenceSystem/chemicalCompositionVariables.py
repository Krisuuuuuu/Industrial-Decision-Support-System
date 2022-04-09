from fuzzy_expert.variable import FuzzyVariable

from core.inferenceSystems.base.baseVariables import BaseVariableWrapper

CHEMICAL_COMPOSITION_VARIABLES: dict[str, FuzzyVariable] = {
    "carbon": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": [(0, 1), (0.1, 1), (0.15, 0), (3.85, 0), (3.9, 1), (100, 1)],
            "Average": [(0, 0), (0.1, 0), (0.15, 1), (3.25, 1), (3.3, 0), (3.75, 0), (3.8, 1), (3.85, 1), (3.9, 0),
                        (100, 0)],
            "Optimal": ('trapmf', 3.25, 3.3, 3.75, 3.8),
        },
    ),
    "sulfur": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": [(0, 1), (0.001, 0), (0.07, 0), (0.071, 1), (100, 1)],
            "Average": ('trapmf', 0.025, 0.03, 0.065, 0.07),
            "Optimal": ('trapmf', 0, 0.001, 0.025, 0.03),
        },
    ),
    "magnesium": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": [(0, 1), (0.25, 1), (0.3, 0), (0.85, 0), (0.9, 1), (100, 1)],
            "Average": [(0, 0), (0.29, 0), (0.3, 1), (0.34, 1), (0.35, 0), (0.74, 0), (0.75, 1), (0.9, 1), (0.91, 0),
                        (100, 0)],
            "Optimal": ('trapmf', 0.34, 0.35, 0.74, 0.75),
        },
    ),
    "silicon": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "Unsuitable": [(0, 1), (1.9, 1), (2, 0), (4.4, 0), (4.5, 1), (100, 1)],
            "Average": [(0, 0), (1.9, 0), (2, 1), (2.1, 1), (2.2, 0), (2.7, 0), (2.8, 1), (4.4, 1), (4.5, 0),
                        (100, 0)],
            "Optimal": ('trapmf', 2, 2.1, 2.7, 2.8),
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
    )
}


class ChemicalCompositionVariableWrapper(BaseVariableWrapper):
    def __init__(self):
        global CHEMICAL_COMPOSITION_VARIABLES
        super().__init__()

    def set_variables(self) -> None:
        self._fuzzy_variables = CHEMICAL_COMPOSITION_VARIABLES
