from .Base.AbstractFactory import AbstractFactory
from ..Builder.Director import Director
from ..Builder.IsothermalTransformationSystemBuilder import IsothermalTransformationInferenceSystemBuilder


class IsothermalTransformationSystemFactory(AbstractFactory):

    def create(self):
        director = Director()
        director.set_builder(IsothermalTransformationInferenceSystemBuilder())
        system_instance = director.get_system_instance()

        return  system_instance
