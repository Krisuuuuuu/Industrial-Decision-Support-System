from matplotlib import pyplot as plt

import core.inferenceSystems.base.baseInferenceSystem as s


class IsothermalTransformationInferenceSystem(s.BaseInferenceSystem):
    def __init__(self, adi_model, variables, rules):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self):
        plt.figure(figsize=(10, 6))
        self._model.plot(
            variables=self.return_fuzzy_variables(),
            rules=self.return_fuzzy_rules(),
            austenitizing_temperature=self._adi_model.austenitizing_temperature,
            isothermal_transformation_temperature=self._adi_model.isothermal_transformation_temperature
        )

        print("Isothermal Transformation Inference System result: ")
        print(self._model(
            variables=self.return_fuzzy_variables(),
            rules=self.return_fuzzy_rules(),
            austenitizing_temperature=self._adi_model.austenitizing_temperature,
            isothermal_transformation_temperature=self._adi_model.isothermal_transformation_temperature
        ))
