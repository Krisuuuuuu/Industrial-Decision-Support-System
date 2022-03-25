from adapter import Adapter
from core.factory.austenitizationProcessSystemFactory import AustenitizationProcessSystemFactory
from core.factory.chemicalCompositionSystemFactory import ChemicalCompositionSystemFactory
from core.factory.isothermalTransformationSystemFactory import IsothermalTransformationSystemFactory
from core.validators.expectedSpeciesValidatorRunner import ExpectedSpeciesValidatorRunner
from core.validators.generalValidatorRunner import GeneralValidatorRunner


class IndustrialDecisionSupportSystem:
    def __init__(self):
        self._inference_system = None
        self._validator_runner = None
        self._adi_model = IndustrialDecisionSupportSystem.set_adi_model()

    @staticmethod
    def set_adi_model():
        adapter = Adapter()
        adi_model = adapter.request()
        return adi_model

    def start_evaluation(self):
        self._run_general_validators()
        self._run_expected_species_validators()
        self._evaluate_chemical_composition()
        self._evaluate_austenitization_process()
        self._evaluate_isothermal_transformation()
        self._dispose_all_components()

    def _run_general_validators(self):
        self._dispose_validator_runner()
        self._validator_runner = GeneralValidatorRunner(self._adi_model)
        self._validator_runner.run()

    def _run_expected_species_validators(self):
        self._dispose_validator_runner()
        self._validator_runner = ExpectedSpeciesValidatorRunner(self._adi_model)
        self._validator_runner.run()

    def _evaluate_chemical_composition(self):
        self._evaluate_inference_system(ChemicalCompositionSystemFactory(self._adi_model))

    def _evaluate_austenitization_process(self):
        self._evaluate_inference_system(AustenitizationProcessSystemFactory(self._adi_model))

    def _evaluate_isothermal_transformation(self):
        self._evaluate_inference_system(IsothermalTransformationSystemFactory(self._adi_model))

    def _evaluate_inference_system(self, abstract_factory):
        self._dispose_inference_system()
        self._prepare_inference_system(abstract_factory)
        self._inference_system.evaluate_results()

    def _prepare_inference_system(self, abstract_factory):
        self._inference_system = abstract_factory.create()

    def _evaluate_results(self):
        self._inference_system.evaluate_results()

    def _dispose_inference_system(self):
        self._inference_system = None

    def _dispose_validator_runner(self):
        self._validator_runner = None

    def _dispose_all_components(self):
        self._dispose_inference_system()
        self._dispose_validator_runner()

