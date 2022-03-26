from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.variable import FuzzyVariable
from matplotlib import pyplot as plt

from core.inferenceSystems.base.baseInferenceSystem import BaseInferenceSystem
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class AustenitizationProcessInferenceSystem(BaseInferenceSystem):
    def __init__(self, adi_model: AdiDuctileIronModel, variables: dict[str, FuzzyVariable], rules: list[FuzzyRule]):
        super().__init__(adi_model, variables, rules)

    def evaluate_results(self) -> None:
        plt.figure(figsize=(10, 6))
        self._model.plot(
            variables=self.fuzzy_variables,
            rules=self.fuzzy_rules,
            austenitization_process_time=self._adi_model.manufacturing_process.austenitization_time,
            wall_thickness=self._adi_model.physical_data.wall_thickness
        )

        self._print_results()

    def _print_results(self) -> None:
        print("Austenitization Process Inference System result: ")
        print(self._model(
            variables=self.fuzzy_variables,
            rules=self.fuzzy_rules,
            austenitization_process_time=self._adi_model.manufacturing_process.austenitization_time,
            wall_thickness=self._adi_model.physical_data.wall_thickness
        ))
        print("\n")
