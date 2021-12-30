from matplotlib import pyplot as plt
import IndustrialDecisionSupportSystemCore.InferenceSystems.Base.BaseInferenceSystem as s


class ChemicalCompositionInferenceSystem(s.BaseInferenceSystem):
    def __init__(self, adi_model, variables, rules):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self):
        plt.figure(figsize=(10, 6))
        self._model.plot(
            variables=self.return_fuzzy_variables(),
            rules=self.return_fuzzy_rules(),
            carbon=self._adiModel.carbon,
            silicon=self._adiModel.silicon,
            manganese=self._adiModel.manganese
        )

        print("Chemical Composition Inference System result: ")
        print(self._model(
            variables=self.return_fuzzy_variables(),
            rules=self.return_fuzzy_rules(),
            carbon=self._adiModel.carbon,
            silicon=self._adiModel.silicon,
            manganese=self._adiModel.manganese
        ))

