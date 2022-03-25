from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType


class IsothermalTransformationTemperatureValueValidator(BaseValidator):
    def __init__(self, model):
        super().__init__(ErrorArea.MANUFACTURING_PROCESS, ErrorType.INVALID_ISOTHERMAL_TEMPERATURE_VALUE, "Isothermal "
                                                                                                          "transformation temperature value validator", model)

    def validate(self):
        self._occurs = self._model.manufacturing_process.isothermal_transformation_temperature <= 0
