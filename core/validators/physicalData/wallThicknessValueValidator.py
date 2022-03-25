from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType


class WallThicknessValueValidator(BaseValidator):
    def __init__(self, model):
        super().__init__(ErrorArea.PHYSICAL_DATA, ErrorType.INVALID_WALL_THICKNESS_VALUE, "Wall thickness value "
                                                                                          "validator", model)

    def validate(self):
        self._occurs = self._model.physical_data.expected_species == ''
