from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class ExpectedSpeciesValueValidator(BaseValidator):
    def __init__(self, model: AdiDuctileIronModel):
        super().__init__(ErrorArea.PHYSICAL_DATA, ErrorType.INVALID_EXPECTED_SPECIES_VALUE,
                         "Expected species value validator", model)

    def validate(self) -> None:
        self._occurs = self._model.physical_data.expected_species == ''
