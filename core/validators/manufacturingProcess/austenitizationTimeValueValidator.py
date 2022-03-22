from core.validators.base.baseValidator import BaseValidator
from core.validators.base.errorArea import ErrorArea
from core.validators.base.errotType import ErrorType


class AustenitizationTimeValueValidator(BaseValidator):
    def __init__(self, model):
        super().__init__(ErrorArea.MANUFACTURING_PROCESS, ErrorType.INVALID_AUSTENIZATION_TEMPERATURE_VALUE, "Austenitization time value validator", model)

    def validate(self):
        self._occurs = self._model.manufacturing_process.austenitization_temperature <= 0