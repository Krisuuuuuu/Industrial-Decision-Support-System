from core.builder.chemicalCompositionSystemBuilder import ChemicalCompositionInferenceSystemBuilder
from core.factory.base.abstractFactory import AbstractFactory
from core.inferenceSystems.chemicalCompositionInferenceSystem.chemicalCompositionInferenceSystem import \
    ChemicalCompositionInferenceSystem
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class ChemicalCompositionSystemFactory(AbstractFactory):
    def __init__(self, model: AdiDuctileIronModel):
        super().__init__(model)

    def create(self) -> ChemicalCompositionInferenceSystem:
        self._director.set_builder(ChemicalCompositionInferenceSystemBuilder())
        return self._director.get_system_instance(self._model)
