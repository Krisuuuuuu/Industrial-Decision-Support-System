from abc import abstractmethod, ABC
from data.adapter.adapter import Adapter


class Builder(ABC):
    @abstractmethod
    def set_variables(self): pass

    @abstractmethod
    def set_rules(self): pass

    @abstractmethod
    def set_system_instance(self, adi_model, variables, rules): pass

    @staticmethod
    def set_adi_model():
        adapter = Adapter()
        adi_model = adapter.request()
        return adi_model
