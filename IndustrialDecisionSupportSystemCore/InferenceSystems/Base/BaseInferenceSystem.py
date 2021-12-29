from abc import abstractmethod, ABC

from fuzzy_expert.inference import DecompositionalInference


class BaseInferenceSystem(ABC):

    @abstractmethod
    def evaluate_results(self): pass

    def __init__(self, adi_model, variables, rules):
        self._adiModel = adi_model
        self._fuzzy_variables = variables
        self._fuzzy_rules = rules
        self._model = None
        self._init_model()

    def return_fuzzy_model(self):
        return self._model

    def return_fuzzy_variables(self):
        return self._fuzzy_variables

    def return_fuzzy_rules(self):
        return self._fuzzy_rules

    def _init_model(self):
        self._model = DecompositionalInference(
            and_operator="min",
            or_operator="max",
            implication_operator="Rc",
            composition_operator="max-min",
            production_link="max",
            defuzzification_operator="cog"
        )
