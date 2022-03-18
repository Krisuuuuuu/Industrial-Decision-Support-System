from core.validators.base.baseValidator import BaseValidator
from core.validators.base.errorArea import ErrorArea
from core.validators.base.errotType import ErrorType


class CarbonValueValidator(BaseValidator):
    def __init__(self, model):
        super().__init__(ErrorArea.CHEMICAL_COMPOSITION, ErrorType.INVALID_CARBON_VALUE, "Carbon value validator", model)

    def validate(self):
        self._occurs = self._model.chemical_composition.carbon <= 0
