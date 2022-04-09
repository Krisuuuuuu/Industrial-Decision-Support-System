from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class SiliconValueValidator(BaseValidator):
    def __init__(self, model: AdiDuctileIronModel):
        super().__init__(ErrorArea.CHEMICAL_COMPOSITION, ErrorType.INVALID_SILICON_VALUE,
                         "Silicon value validator", model)

    def validate(self) -> None:
        self._occurs = self._model.chemical_composition.silicon <= 0 or self._model.chemical_composition.silicon > 100
