from fuzzy_expert.inference import DecompositionalInference

class BaseInferenceSystem:
    def evaluateResults(self): pass

    def __init__(self, adiModel, variables, rules):
        self.__adiModel = adiModel
        self.__fuzzy_variables = variables
        self.__fuzzy_rules = rules
        self.__initModel()

    def __initModel(self):
        self.__model = DecompositionalInference(
            and_operator="min",
            or_operator="max",
            implication_operator="Rc",
            composition_operator="max-min",
            production_link="max",
            defuzzification_operator="cog"
        )

    def returnFuzzyModel(self):
        return self.__model

    def returnFuzzyVariables(self):
        return self.__fuzzy_variables

    def returnFuzzyRules(self):
        return self.__fuzzy_rules
    