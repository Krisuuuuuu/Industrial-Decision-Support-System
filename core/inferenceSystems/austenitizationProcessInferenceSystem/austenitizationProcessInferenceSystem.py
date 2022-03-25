from matplotlib import pyplot as plt

import core.inferenceSystems.base.baseInferenceSystem as s


class AustenitizationProcessInferenceSystem(s.BaseInferenceSystem):
    def __init__(self, adi_model, variables, rules):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self):
        plt.figure(figsize=(10, 6))
        self._model.plot(
            variables=self.fuzzy_variables,
            rules=self.fuzzy_rules,
            austenitization_process_time=self._adi_model.manufacturing_process.austenitization_time,
            wall_thickness=self._adi_model.physical_data.wall_thickness
        )

        print("Austenitization Process Inference System result: ")
        print(self._model.plot(
            variables=self.fuzzy_variables,
            rules=self.fuzzy_rules,
            austenitization_process_time=self._adi_model.manufacturing_process.austenitization_time,
            wall_thickness=self._adi_model.physical_data.wall_thickness
        ))
        print("\n")
