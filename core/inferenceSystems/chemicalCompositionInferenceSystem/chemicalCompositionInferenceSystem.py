from matplotlib import pyplot as plt

from core.inferenceSystems.base.baseInferenceSystem import BaseInferenceSystem


class ChemicalCompositionInferenceSystem(BaseInferenceSystem):
    def __init__(self, adi_model, variables, rules):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self):
        plt.figure(figsize=(10, 6))
        self._model.plot(
            variables=self.fuzzy_variables,
            rules=self.fuzzy_rules,
            carbon=self._adi_model.chemical_composition.carbon,
            silicon=self._adi_model.chemical_composition.silicon,
            magnesium=self._adi_model.chemical_composition.magnesium,
            sulfur=self._adi_model.chemical_composition.sulfur
        )

        print("Chemical Composition Inference System result: ")
        print(self._model(
            variables=self.fuzzy_variables,
            rules=self.fuzzy_rules,
            carbon=self._adi_model.chemical_composition.carbon,
            silicon=self._adi_model.chemical_composition.silicon,
            magnesium=self._adi_model.chemical_composition.magnesium,
            sulfur=self._adi_model.chemical_composition.sulfur
        ))
