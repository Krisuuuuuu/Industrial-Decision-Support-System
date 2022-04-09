from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.variable import FuzzyVariable

from core.builder.base.builder import Builder
from core.inferenceSystems.base.baseInferenceSystem import BaseInferenceSystem
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class Director:
    def __init__(self):
        self._builder: Builder = None

    def set_builder(self, builder: Builder) -> None:
        self._builder = builder

    def get_system_instance(self, model: AdiDuctileIronModel) -> BaseInferenceSystem:
        variables: dict[str, FuzzyVariable] = self._builder.set_variables()
        rules: list[FuzzyRule] = self._builder.set_rules()
        adi_model: AdiDuctileIronModel = model
        return self._builder.set_system_instance(adi_model, variables, rules)
