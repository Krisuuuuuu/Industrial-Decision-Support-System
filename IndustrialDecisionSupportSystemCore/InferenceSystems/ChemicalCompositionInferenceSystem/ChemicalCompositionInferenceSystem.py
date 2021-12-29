from ..Base.BaseInferenceSystem import BaseInferenceSystem


class ChemicalCompositionInferenceSystem(BaseInferenceSystem):
    def __init__(self, adi_model, variables, rules):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self):
        self._model(
            variables=self.return_fuzzy_variables(),
            rules=self.return_fuzzy_rules(),
            carbon=self._adiModel.carbon,
            silicon=self._adiModel.silicon,
            manganese=self._adiModel.manganese
        )
