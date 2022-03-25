from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType


class IsothermalTransformationTimeValueValidator(BaseValidator):
    def __init__(self, model):
        super().__init__(ErrorArea.MANUFACTURING_PROCESS, ErrorType.INVALID_ISOTHERMAL_TIME_VALUE, "Isothermal "
                                                                                                   "transformation "
                                                                                                   "time value "
                                                                                                   "validator", model)

    def validate(self):
        self._occurs = self._model.manufacturing_process.isothermal_transformation_time <= 0
