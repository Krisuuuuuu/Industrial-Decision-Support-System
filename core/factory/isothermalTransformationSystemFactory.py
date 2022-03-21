from core.builder.isothermalTransformationSystemBuilder import IsothermalTransformationInferenceSystemBuilder
from core.factory.base.abstractFactory import AbstractFactory


class IsothermalTransformationSystemFactory(AbstractFactory):
    def __init__(self, model):
        super().__init__(model)

    def create(self):
        self._director.set_builder(IsothermalTransformationInferenceSystemBuilder())
        system_instance = self._director.get_system_instance(self._model)

        return system_instance
