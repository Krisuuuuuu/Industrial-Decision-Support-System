from core.builder.austenitizationProcessSystemBuilder import AustenitizationProcessInferenceSystemBuilder
from core.factory.base.abstractFactory import AbstractFactory
from core.inferenceSystems.austenitizationProcessInferenceSystem.austenitizationProcessInferenceSystem import \
    AustenitizationProcessInferenceSystem
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class AustenitizationProcessSystemFactory(AbstractFactory):
    def __init__(self, model: AdiDuctileIronModel):
        super().__init__(model)

    def create(self) -> AustenitizationProcessInferenceSystem:
        self._director.set_builder(AustenitizationProcessInferenceSystemBuilder())
        return self._director.get_system_instance(self._model)
