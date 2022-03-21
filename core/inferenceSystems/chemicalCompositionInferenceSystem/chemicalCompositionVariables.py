from fuzzy_expert.variable import FuzzyVariable

from core.inferenceSystems.base.baseVariables import BaseVariableWrapper

CHEMICAL_COMPOSITION_VARIABLES = {

}


class ChemicalCompositionVariableWrapper(BaseVariableWrapper):
    def __init__(self):
        global CHEMICAL_COMPOSITION_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = CHEMICAL_COMPOSITION_VARIABLES

