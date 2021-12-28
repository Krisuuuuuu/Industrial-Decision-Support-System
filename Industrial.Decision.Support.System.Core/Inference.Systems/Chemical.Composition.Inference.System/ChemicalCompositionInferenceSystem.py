from fuzzy_expert.inference import DecompositionalInference

class ChemicalCompositionInferenceSystem:
    def __init__(self, adiModel, variables, rules):
        super.__init__(adiModel, variables, rules)

    def evaluateResults(self):
        self.__model(
            variables=self.__returnFuzzyVariables(),
            rules=self.__returnFuzzyRules(),
            carbon=self.__adiModel.carbon,
            silicon=self.__adiModel.silicon,
            manganese=self.__adiModel.manganese
        )
    