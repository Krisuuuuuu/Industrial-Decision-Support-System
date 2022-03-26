from abc import abstractmethod, ABC

from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class BaseValidator(ABC):
    @abstractmethod
    def validate(self) -> None: pass

    def __init__(self, error_area: ErrorArea, error_type: ErrorType, name: str, model: AdiDuctileIronModel):
        self.ErrorArea: ErrorArea = error_area
        self.ErrorType: ErrorType = error_type
        self._name: str = name
        self._model: AdiDuctileIronModel = model
        self._occurs: bool = False

    @property
    def name(self) -> str:
        return self._name

    @property
    def occurs(self) -> bool:
        return self._occurs
