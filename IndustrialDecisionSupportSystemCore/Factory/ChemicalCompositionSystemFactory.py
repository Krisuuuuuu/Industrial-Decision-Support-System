from .Base.AbstractFactory import AbstractFactory
from ..Builder.ChemicalCompositionSystemBuilder import ChemicalCompositionInferenceSystemBuilder


class ChemicalCompositionSystemFactory(AbstractFactory):
    def __init__(self):
        super().__init__()

    def create(self):
        self._director.set_builder(ChemicalCompositionInferenceSystemBuilder())
        system_instance = self._director.get_system_instance()

        return system_instance
