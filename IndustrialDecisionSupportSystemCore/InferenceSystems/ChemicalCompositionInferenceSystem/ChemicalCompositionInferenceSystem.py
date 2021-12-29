from ..Base.BaseInferenceSystem import BaseInferenceSystem


class ChemicalCompositionInferenceSystem(BaseInferenceSystem):
    def __init__(self, adi_model, variables, rules):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self):
        self.__model(
            variables=self.__returnFuzzyVariables(),
            rules=self.__returnFuzzyRules(),
            carbon=self.__adiModel.carbon,
            silicon=self.__adiModel.silicon,
            manganese=self.__adiModel.manganese
        )
