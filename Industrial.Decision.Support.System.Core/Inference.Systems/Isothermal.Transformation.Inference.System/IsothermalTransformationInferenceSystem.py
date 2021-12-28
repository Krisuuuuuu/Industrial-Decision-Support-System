from fuzzy_expert.inference import DecompositionalInference

class IsothermalTransformationInferenceSystem:
    def __init__(self, adiModel, variables, rules):
        super.__init__(adiModel, variables, rules)

    def evaluateResults(self):
        self.__model(
            variables=self.__returnFuzzyVariables(),
            rules=self.__returnFuzzyRules(),
            austenitizing_temperature = self.__adiModel.austenitizing_temperature,
            isothermal_transformation_temperature = self.__adiModel.isothermal_transformation_temperature
        )