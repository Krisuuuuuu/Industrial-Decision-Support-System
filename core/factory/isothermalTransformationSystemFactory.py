from core.builder.isothermalTransformationSystemBuilder import IsothermalTransformationInferenceSystemBuilder
from core.factory.base.abstractFactory import AbstractFactory
from core.inferenceSystems.isothermalTransformationInferenceSystem.isothermalTransformationInferenceSystem import \
    IsothermalTransformationInferenceSystem
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class IsothermalTransformationSystemFactory(AbstractFactory):
    def __init__(self, model: AdiDuctileIronModel):
        super().__init__(model)

    def create(self) -> IsothermalTransformationInferenceSystem:
        self._director.set_builder(IsothermalTransformationInferenceSystemBuilder())
        return self._director.get_system_instance(self._model)
