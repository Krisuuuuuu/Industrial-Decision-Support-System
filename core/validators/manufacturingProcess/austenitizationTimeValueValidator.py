from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType


class AustenitizationTimeValueValidator(BaseValidator):
    def __init__(self, model):
        super().__init__(ErrorArea.MANUFACTURING_PROCESS, ErrorType.INVALID_AUSTENIZATION_TEMPERATURE_VALUE,
                         "Austenitization time value validator", model)

    def validate(self):
        self._occurs = self._model.manufacturing_process.austenitization_time <= 0
