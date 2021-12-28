from .Variables import Variables as v
from .Rules import Rules as r
from fuzzy_expert.inference import DecompositionalInference

class ChemicalCompositionInferenceSystem:
    def __init__(self, adiModel):
        self.__adiModel = adiModel
        self.__initWrappers()
        self.__fuzzy_variables = self.__variablesWrapper.getChemicalCompositionVariables()
        self.__fuzzy_rules = self.__rulesWrapper.getChemicalCompositionRules()
        self.__initModel()

    def evaluateResults(self):
        self.__model(
            variables=self.__returnFuzzyVariables(),
            rules=self.__returnFuzzyRules(),
            carbon=self.__adiModel.carbon,
            silicon=self.__adiModel.silicon,
            manganese=self.__adiModel.manganese
        )

    def returnFuzzyModel(self):
        return self.__model

    def __returnFuzzyVariables(self):
        return self.__fuzzy_variables

    def __returnFuzzyRules(self):
        return self.__fuzzy_rules

    def __initWrappers(self):
        self.__variablesWrapper = v.ChemicalCompositionVariableWrapper()
        self.__rulesWrapper = r.ChemicalCompositionRulesWrapper()

    def __initModel(self):
        self.__model = DecompositionalInference(
            and_operator="min",
            or_operator="max",
            implication_operator="Rc",
            composition_operator="max-min",
            production_link="max",
            defuzzification_operator="cog"
        )
    