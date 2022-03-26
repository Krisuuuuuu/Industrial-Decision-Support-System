from abc import abstractmethod, ABC
from fuzzy_expert.inference import DecompositionalInference
from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.variable import FuzzyVariable

from data.models.adiDuctileIronModel import AdiDuctileIronModel


class BaseInferenceSystem(ABC):
    @abstractmethod
    def evaluate_results(self) -> None: pass

    @abstractmethod
    def _print_results(self) -> None: pass

    def __init__(self, adi_model: AdiDuctileIronModel, variables: dict[str, FuzzyVariable], rules: list[FuzzyRule]):
        self._adi_model: AdiDuctileIronModel = adi_model
        self._fuzzy_variables: dict[str, FuzzyVariable] = variables
        self._fuzzy_rules: list[FuzzyRule] = rules
        self._model: DecompositionalInference = None
        self._init_model()

    @property
    def fuzzy_model(self) -> AdiDuctileIronModel:
        return self._model

    @property
    def fuzzy_variables(self) -> dict[str, FuzzyVariable]:
        return self._fuzzy_variables

    @property
    def fuzzy_rules(self) -> list[FuzzyRule]:
        return self._fuzzy_rules

    def _init_model(self) -> None:
        self._model = DecompositionalInference(
            and_operator="min",
            or_operator="max",
            implication_operator="Rc",
            composition_operator="max-min",
            production_link="max",
            defuzzification_operator="cog",
        )
