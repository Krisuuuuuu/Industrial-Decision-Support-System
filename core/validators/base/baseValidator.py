from abc import abstractmethod, ABC


class BaseValidator(ABC):
    def __init__(self, error_area, error_type, name, model):
        self.ErrorArea = error_area
        self.ErrorType = error_type
        self._name = name
        self._model = model
        self._occurs = False

    @abstractmethod
    def validate(self): pass

