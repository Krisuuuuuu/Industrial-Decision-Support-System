from adapter import Adapter
from core.factory.austenitizationProcessSystemFactory import AustenitizationProcessSystemFactory
from core.factory.isothermalTransformationSystemFactory import IsothermalTransformationSystemFactory
from core.validators.generalValidatorRunner import GeneralValidatorRunner


class IndustrialDecisionSupportSystem:
    def __init__(self):
        self._inference_system = None
        self._adi_model = IndustrialDecisionSupportSystem.set_adi_model()
        self._general_validator_runner = GeneralValidatorRunner(self._adi_model)

    @staticmethod
    def set_adi_model():
        adapter = Adapter()
        adi_model = adapter.request()
        return adi_model

    def start_evaluation(self):
        self._run_general_validators()
        self._evaluate_austenitization_process()
        self._evaluate_isothermal_transformation()

    def _run_general_validators(self):
        self._general_validator_runner.run()

    def _evaluate_austenitization_process(self):
        self._dispose_inference_system()
        self._prepare_inference_system(AustenitizationProcessSystemFactory(self._adi_model))
        self._inference_system.evaluate_results()

    def _evaluate_isothermal_transformation(self):
        self._dispose_inference_system()
        self._prepare_inference_system(IsothermalTransformationSystemFactory(self._adi_model))
        self._inference_system.evaluate_results()

    def _prepare_inference_system(self, abstract_factory):
        self._inference_system = abstract_factory.create()

    def _evaluate_results(self):
        self._inference_system.evaluate_results()

    def _dispose_inference_system(self):
        self._inference_system = None

