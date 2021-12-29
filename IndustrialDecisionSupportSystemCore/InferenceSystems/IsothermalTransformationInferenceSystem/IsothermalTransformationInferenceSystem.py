from ..Base.BaseInferenceSystem import BaseInferenceSystem


class IsothermalTransformationInferenceSystem(BaseInferenceSystem):
    def __init__(self, adi_model, variables, rules):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self):
        self._model(
            variables=self.return_fuzzy_variables(),
            rules=self.return_fuzzy_rules(),
            austenitizing_temperature=self._adiModel.austenitizing_temperature,
            isothermal_transformation_temperature=self._adiModel.isothermal_transformation_temperature
        )
