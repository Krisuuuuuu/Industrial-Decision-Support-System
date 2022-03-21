from core.builder.chemicalCompositionSystemBuilder import ChemicalCompositionInferenceSystemBuilder
from core.factory.base.abstractFactory import AbstractFactory


class ChemicalCompositionSystemFactory(AbstractFactory):
    def __init__(self, model):
        super().__init__(model)

    def create(self):
        self._director.set_builder(ChemicalCompositionInferenceSystemBuilder())
        system_instance = self._director.get_system_instance(self._model)

        return system_instance
