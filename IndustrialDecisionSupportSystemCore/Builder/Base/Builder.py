from abc import abstractmethod, ABC


class Builder(ABC):
    @abstractmethod
    def set_variables(self): pass

    @abstractmethod
    def set_rules(self): pass

    @abstractmethod
    def set_adi_model(self): pass

    @abstractmethod
    def set_system_instance(self, adi_model, variables, rules): pass
