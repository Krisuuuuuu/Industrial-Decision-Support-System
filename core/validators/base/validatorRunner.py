from abc import ABC, abstractmethod


class BaseValidatorRunner(ABC):
    def __init__(self, model):
        self._model = model
        self._validators = self._initValidators()

    @abstractmethod
    def _initValidators(self): pass

    @abstractmethod
    def run(self): pass

    @property
    def validators(self):
        return self._validators
