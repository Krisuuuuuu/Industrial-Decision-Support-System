from fuzzy_expert.variable import FuzzyVariable
import IndustrialDecisionSupportSystemCore.InferenceSystems.Base.BaseVariables as v

MATERIAL_DEFECTS_VARIABLES = {}


class MaterialDefectsVariableWrapper(v.BaseVariableWrapper):
    def __init__(self):
        global MATERIAL_DEFECTS_VARIABLES
        super().__init__()

    def set_variables(self):
        self._fuzzy_variables = MATERIAL_DEFECTS_VARIABLES

