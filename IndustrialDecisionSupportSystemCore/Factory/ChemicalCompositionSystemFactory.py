from .Base.AbstractFactory import AbstractFactory
from ..Builder.Director import Director
from ..Builder.ChemicalCompositionSystemBuilder import ChemicalCompositionInferenceSystemBuilder


class ChemicalCompositionSystemFactory(AbstractFactory):

    def create(self):
        director = Director()
        director.set_builder(ChemicalCompositionInferenceSystemBuilder())
        system_instance = director.get_system_instance()

        return  system_instance
