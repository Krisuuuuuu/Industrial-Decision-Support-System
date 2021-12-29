from .Base.AbstractFactory import AbstractFactory
from ..Builder.IsothermalTransformationSystemBuilder import IsothermalTransformationInferenceSystemBuilder


class IsothermalTransformationSystemFactory(AbstractFactory):
    def __init__(self):
        super().__init__()

    def create(self):
        self._director.set_builder(IsothermalTransformationInferenceSystemBuilder())
        system_instance = self._director.get_system_instance()

        return  system_instance
