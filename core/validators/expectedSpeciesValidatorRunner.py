from core.validators.base.baseValidator import BaseValidator
from core.validators.base.validatorRunner import BaseValidatorRunner
from core.validators.expectedSpecies.expectedSpeciesAustenitizationTemperatureValidator import \
    ExpectedSpeciesAustenizationTemperatureValidator
from core.validators.expectedSpecies.expectedSpeciesIsothermalTransformationTemperatureValidator import \
    ExpectedSpeciesIsothermalTransformationValidator
from core.validators.expectedSpecies.models.ductileIronSpeciesEnum import DuctileIronSpecies
from core.validators.expectedSpecies.models.species import Species
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class ExpectedSpeciesValidatorRunner(BaseValidatorRunner):
    def __init__(self, model: AdiDuctileIronModel):
        super().__init__(model)

    def _initValidators(self) -> list[BaseValidator]:
        species: Species = self._setDuctileIronSpecies()

        if species is not None:
            return [
                ExpectedSpeciesAustenizationTemperatureValidator(self._model, species),
                ExpectedSpeciesIsothermalTransformationValidator(self._model, species)
            ]
        else:
            return []

    def _setDuctileIronSpecies(self) -> Species:
        if self._model.physical_data.expected_species == 'GJS 800-10':
            return Species(DuctileIronSpecies.GJS_800_10, 860, 920, 380, 400)
        elif self._model.physical_data.expected_species == 'GJS 1200-3':
            return Species(DuctileIronSpecies.GJS_1200_3, 880, 950, 340, 370)
        elif self._model.physical_data.expected_species == 'GJS 1400-1':
            return Species(DuctileIronSpecies.GJS_1400_1, 890, 950, 270, 290)
        else:
            return None

    def print_failed_validators(self) -> None:
        print("Failed expected species validators: ")
        super().print_failed_validators()
        print("\n")
