from matplotlib import pyplot as plt
import Core.InferenceSystems.Base.BaseInferenceSystem as s


class ChemicalCompositionInferenceSystem(s.BaseInferenceSystem):
    def __init__(self, adi_model, variables, rules):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self):
        plt.figure(figsize=(10, 6))
        self._model.plot(
            variables=self.return_fuzzy_variables(),
            rules=self.return_fuzzy_rules(),
            carbon=self._adi_model.carbon,
            silicon=self._adi_model.silicon,
            manganese=self._adi_model.manganese
        )

        print("Chemical Composition Inference System result: ")
        print(self._model(
            variables=self.return_fuzzy_variables(),
            rules=self.return_fuzzy_rules(),
            carbon=self._adi_model.carbon,
            silicon=self._adi_model.silicon,
            manganese=self._adi_model.manganese
        ))

