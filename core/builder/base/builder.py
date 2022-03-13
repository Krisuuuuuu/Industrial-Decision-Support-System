from abc import abstractmethod, ABC
import data.models.adiDuctileIronModel as m
from data.adapter.adapter import Adapter


class Builder(ABC):
    @abstractmethod
    def set_variables(self): pass

    @abstractmethod
    def set_rules(self): pass

    @abstractmethod
    def set_system_instance(self, adi_model, variables, rules): pass

    def set_adi_model(self):
        adapter = Adapter()
        adi_model = adapter.request()
        return adi_model
