from adapter import Adapter
from core.factory.austenitizationProcessSystemFactory import AustenitizationProcessSystemFactory
from core.factory.base.abstractFactory import AbstractFactory
from core.factory.chemicalCompositionSystemFactory import ChemicalCompositionSystemFactory
from core.factory.isothermalTransformationSystemFactory import IsothermalTransformationSystemFactory
from core.inferenceSystems.base.baseInferenceSystem import BaseInferenceSystem
from core.validators.base.validatorRunner import BaseValidatorRunner
from core.validators.expectedSpeciesValidatorRunner import ExpectedSpeciesValidatorRunner
from core.validators.generalValidatorRunner import GeneralValidatorRunner
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class IndustrialDecisionSupportSystem:
    def __init__(self):
        self._inference_system: BaseInferenceSystem = None
        self._validator_runner: BaseValidatorRunner = None
        self._adi_model: AdiDuctileIronModel = IndustrialDecisionSupportSystem._set_adi_model()

    @staticmethod
    def _set_adi_model():
        adapter: Adapter = Adapter()
        return adapter.request()

    def start_evaluation(self) -> None:
        self._run_general_validators()
        self._run_expected_species_validators()
        self._evaluate_chemical_composition()
        self._evaluate_austenitization_process()
        self._evaluate_isothermal_transformation()
        self._dispose_all_components()

    def _run_validators(self, validator_runner: BaseValidatorRunner) -> None:
        self._validator_runner: BaseValidatorRunner = validator_runner
        self._validator_runner.run()
        self._validator_runner.print_failed_validators()

    def _run_general_validators(self) -> None:
        self._dispose_validator_runner()
        self._run_validators(GeneralValidatorRunner(self._adi_model))

    def _run_expected_species_validators(self) -> None:
        self._dispose_validator_runner()
        self._run_validators(ExpectedSpeciesValidatorRunner(self._adi_model))

    def _evaluate_inference_system(self, abstract_factory: AbstractFactory) -> None:
        self._dispose_inference_system()
        self._prepare_inference_system(abstract_factory)
        self._inference_system.evaluate_results()

    def _evaluate_chemical_composition(self) -> None:
        self._evaluate_inference_system(ChemicalCompositionSystemFactory(self._adi_model))

    def _evaluate_austenitization_process(self) -> None:
        self._evaluate_inference_system(AustenitizationProcessSystemFactory(self._adi_model))

    def _evaluate_isothermal_transformation(self) -> None:
        self._evaluate_inference_system(IsothermalTransformationSystemFactory(self._adi_model))

    def _prepare_inference_system(self, abstract_factory: AbstractFactory) -> None:
        self._inference_system = abstract_factory.create()

    def _evaluate_results(self) -> None:
        self._inference_system.evaluate_results()

    def _dispose_inference_system(self) -> None:
        self._inference_system = None

    def _dispose_validator_runner(self) -> None:
        self._validator_runner = None

    def _dispose_all_components(self) -> None:
        self._dispose_inference_system()
        self._dispose_validator_runner()
