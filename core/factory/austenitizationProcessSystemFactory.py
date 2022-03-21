from core.builder.austenitizationProcessSystemBuilder import AustenitizationProcessInferenceSystemBuilder
from core.factory.base.abstractFactory import AbstractFactory


class AustenitizationProcessSystemFactory(AbstractFactory):
    def __init__(self, model):
        super().__init__(model)

    def create(self):
        self._director.set_builder(AustenitizationProcessInferenceSystemBuilder())
        system_instance = self._director.get_system_instance(self._model)

        return system_instance
