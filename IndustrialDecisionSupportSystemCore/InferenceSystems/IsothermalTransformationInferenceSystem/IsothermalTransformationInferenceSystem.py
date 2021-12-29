from ..Base.BaseInferenceSystem import BaseInferenceSystem


class IsothermalTransformationInferenceSystem(BaseInferenceSystem):
    def __init__(self, adi_model, variables, rules):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self):
        self.__model(
            variables=self.__returnFuzzyVariables(),
            rules=self.__returnFuzzyRules(),
            austenitizing_temperature=self.__adiModel.austenitizing_temperature,
            isothermal_transformation_temperature=self.__adiModel.isothermal_transformation_temperature
        )
