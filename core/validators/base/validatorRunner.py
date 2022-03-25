from abc import ABC, abstractmethod


class BaseValidatorRunner(ABC):
    def __init__(self, model):
        self._model = model
        self._validators = self._initValidators()

    @abstractmethod
    def _initValidators(self): pass

    @property
    def validators(self):
        return self._validators

    def run(self):
        for validator in self.validators:
            validator.validate()
