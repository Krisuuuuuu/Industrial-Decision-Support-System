from abc import ABC, abstractmethod


class BaseValidatorRunner(ABC):
    def __init__(self, model):
        self._model = model
        self._validators = self._initValidators()
        self._failed_validators = []

    @abstractmethod
    def _initValidators(self): pass

    @property
    def validators(self):
        return self._validators

    def run(self):
        for validator in self.validators:
            validator.validate()

    def _get_failed_validators(self):
        for validator in self.validators:
            if validator.occurs:
                self._failed_validators.append(validator)

    def print_failed_validators(self):
        self._get_failed_validators()

        if len(self._failed_validators) == 0:
            print("Everything went well.")
            return

        for validator in self._failed_validators:
            print(validator.name)