from abc import abstractmethod, ABC
import IndustrialDecisionSupportSystemData.AdiDuctileIronModel as m


class Builder(ABC):
    @abstractmethod
    def set_variables(self): pass

    @abstractmethod
    def set_rules(self): pass

    @abstractmethod
    def set_system_instance(self, adi_model, variables, rules): pass

    def set_adi_model(self):
        adi_model = m.AdiDuctileIronModel(2, 0.6, 930, 235, 3.62, 2.50, 0.45)
        return adi_model
