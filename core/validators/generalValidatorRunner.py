from core.validators.base.validatorRunner import BaseValidatorRunner
from core.validators.chemicalComposition.carbonValueValidator import CarbonValueValidator
from core.validators.chemicalComposition.magnesiumValueValidator import MagnesiumValueValidator
from core.validators.chemicalComposition.siliconValueValidator import SiliconValueValidator
from core.validators.chemicalComposition.sulfurValueValidator import SulfurValueValidator
from core.validators.manufacturingProcess.austenitizationTemperatureValueValidator import \
    AustenitizationTemperatureValueValidator
from core.validators.manufacturingProcess.austenitizationTimeValueValidator import AustenitizationTimeValueValidator
from core.validators.manufacturingProcess.isothermalTransformationTemperatureValueValidator import \
    IsothermalTransformationTemperatureValueValidator
from core.validators.manufacturingProcess.isothermalTransformationTimeValueValidator import \
    IsothermalTransformationTimeValueValidator
from core.validators.physicalData.expectedSpeciesValueValidator import ExpectedSpeciesValueValidator
from core.validators.physicalData.wallThicknessValueValidator import WallThicknessValueValidator


class GeneralValidatorRunner(BaseValidatorRunner):
    def __init__(self, model):
        super().__init__(model)

    def _initValidators(self):
        return [
            CarbonValueValidator(self._model),
            MagnesiumValueValidator(self._model),
            SiliconValueValidator(self._model),
            SulfurValueValidator(self._model),
            AustenitizationTemperatureValueValidator(self._model),
            AustenitizationTimeValueValidator(self._model),
            IsothermalTransformationTemperatureValueValidator(self._model),
            IsothermalTransformationTimeValueValidator(self._model),
            ExpectedSpeciesValueValidator(self._model),
            WallThicknessValueValidator(self._model),
        ]

    def run(self):
        for validator in self.validators:
            validator.validate()
