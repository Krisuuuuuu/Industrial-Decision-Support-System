from core.factory.isothermalTransformationSystemFactory import IsothermalTransformationSystemFactory


class IndustrialDecisionSupportSystem:
    def __init__(self):
        self._inference_system = None

    def start_evaluation(self):
        self._evaluate_isothermal_transformation()

    def _evaluate_isothermal_transformation(self):
        self._dispose_inference_system()
        self._prepare_inference_system(IsothermalTransformationSystemFactory())
        self._inference_system.evaluate_results()

    def _prepare_inference_system(self, abstract_factory):
        self._inference_system = abstract_factory.create()

    def _evaluate_results(self):
        self._inference_system.evaluate_results()

    def _dispose_inference_system(self):
        self._inference_system = None
