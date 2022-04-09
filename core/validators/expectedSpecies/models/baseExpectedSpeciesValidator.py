from abc import abstractmethod

from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType
from core.validators.expectedSpecies.models.species import Species
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class BaseExpectedSpeciesValidator(BaseValidator):
    @abstractmethod
    def validate(self) -> None: pass

    def __init__(self, error_type: ErrorType, name: str, model: AdiDuctileIronModel, species_model: Species):
        self._species_model: Species = species_model
        super().__init__(ErrorArea.EXPECTED_SPECIES, error_type, name, model)

