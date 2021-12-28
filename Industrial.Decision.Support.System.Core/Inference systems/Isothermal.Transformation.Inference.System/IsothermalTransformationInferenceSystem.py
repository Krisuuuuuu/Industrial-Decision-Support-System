from .Variables import Variables as v
from .Rules import Rules as r
from fuzzy_expert.inference import DecompositionalInference

class IsothermalTransformationInferenceSystem:
    def __init__(self, adiModel):
        self.__adiModel = adiModel
        self.__initWrappers()
        self.__fuzzy_variables = self.__variablesWrapper.getIsothermalTransformationVariables()
        self.__fuzzy_rules = self.__rulesWrapper.getIsothermalTransformationRules()
        self.__initModel()

    def returnFuzzyModel(self):
        return self.__model

    def __returnFuzzyVariables(self):
        return self.__fuzzy_variables

    def __returnFuzzyRules(self):
        return self.__fuzzy_rules

    def __initWrappers(self):
        self.__variablesWrapper = v.IsothermalTransformationVariableWrapper()
        self.__rulesWrapper = r.IsothermalTransformationRulesWrapper()

    def __initModel(self):
        self.__model = DecompositionalInference(
            and_operator="min",
            or_operator="max",
            implication_operator="Rc",
            composition_operator="max-min",
            production_link="max",
            defuzzification_operator="cog"
        )
        self.__model(
            variables=self.__returnFuzzyVariables(),
            rules=self.__returnFuzzyRules(),
            austenitizing_temperature = self.__adiModel.austenitizing_temperature,
            isothermal_transformation_temperature = self.__adiModel.isothermal_transformation_temperature
        )

    