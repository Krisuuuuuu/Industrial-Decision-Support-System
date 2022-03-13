from abc import abstractmethod, ABC
import Data.Models.AdiDuctileIronModel as m
from Data.Adapter.Adapter import Adapter


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
