from abc import abstractmethod, ABC

from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.variable import FuzzyVariable

from core.inferenceSystems.base.baseInferenceSystem import BaseInferenceSystem
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class Builder(ABC):
    @abstractmethod
    def set_variables(self) -> dict[str, FuzzyVariable]: pass

    @abstractmethod
    def set_rules(self) -> list[FuzzyRule]: pass

    @abstractmethod
    def set_system_instance(self, adi_model: AdiDuctileIronModel, variables: dict[str, FuzzyVariable],
                            rules: list[FuzzyRule]) -> BaseInferenceSystem: pass
