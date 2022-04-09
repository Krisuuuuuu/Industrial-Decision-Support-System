from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class IsothermalTransformationTemperatureValueValidator(BaseValidator):
    def __init__(self, model: AdiDuctileIronModel):
        super().__init__(ErrorArea.MANUFACTURING_PROCESS, ErrorType.INVALID_ISOTHERMAL_TEMPERATURE_VALUE,
                         "Isothermal transformation temperature value validator", model)

    def validate(self) -> None:
        self._occurs = self._model.manufacturing_process.isothermal_transformation_temperature <= 0 or self._model.manufacturing_process.isothermal_transformation_temperature > 500
