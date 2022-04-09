from abc import ABC, abstractmethod

from core.validators.base.baseValidator import BaseValidator
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class BaseValidatorRunner(ABC):
    @abstractmethod
    def _initValidators(self) -> list[BaseValidator]: pass

    def __init__(self, model: AdiDuctileIronModel):
        self._model: AdiDuctileIronModel = model
        self._validators: list[BaseValidator] = self._initValidators()
        self._failed_validators: list[BaseValidator] = []

    def _get_failed_validators(self) -> None:
        for validator in self.validators:
            if validator.occurs:
                self._failed_validators.append(validator)

    @property
    def validators(self) -> list[BaseValidator]:
        return self._validators

    @property
    def failed_validators(self) -> list[BaseValidator]:
        return self._failed_validators

    def run(self) -> None:
        for validator in self.validators:
            validator.validate()

    def print_failed_validators(self) -> None:
        self._get_failed_validators()

        if len(self._failed_validators) == 0:
            print("Everything went well.")
            return

        for validator in self._failed_validators:
            print(validator.name)
