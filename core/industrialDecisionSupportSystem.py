from core.imageAnalysis.analyzer import Analyzer
from imageAdapter import ImageAdapter
from modelAdapter import ModelAdapter
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
        self._analyzer: Analyzer = Analyzer()
        self._adi_model: AdiDuctileIronModel = IndustrialDecisionSupportSystem._set_adi_model()

    @staticmethod
    def _set_adi_model() -> AdiDuctileIronModel:
        adapter: ModelAdapter = ModelAdapter()
        return adapter.request()

    @staticmethod
    def _set_test_data(adapter: ImageAdapter) -> None:
        return adapter.request()

    @staticmethod
    def _set_train_data(adapter: ImageAdapter) -> None:
        return adapter.train_data_request()

    def start_evaluation(self) -> None:
        self._run_general_validators()

        if not(self._check_general_validators()):
            print("At least one of general validators failed. Check your input data and try again.")
            return

        self._run_expected_species_validators()
        self._evaluate_chemical_composition()
        self._evaluate_austenitization_process()
        self._evaluate_isothermal_transformation()

        self._run_images_analysis()

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

    def _check_general_validators(self) -> bool:
        return len(self._validator_runner.failed_validators) == 0

    def _evaluate_inference_system(self, abstract_factory: AbstractFactory) -> None:
        self._dispose_inference_system()
        self._prepare_inference_system(abstract_factory)
        self._evaluate_results()

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

    def _run_images_analysis(self) -> None:
        self._set_image_data()

    def _set_image_data(self) -> None:
        adapter: ImageAdapter = ImageAdapter()
        self._analyzer.set_image_data(IndustrialDecisionSupportSystem._set_test_data(adapter),
                                      IndustrialDecisionSupportSystem._set_train_data(adapter))

    def _dispose_inference_system(self) -> None:
        self._inference_system = None

    def _dispose_validator_runner(self) -> None:
        self._validator_runner = None

    def _dispose_analyzer(self) -> None:
        self._analyzer = None

    def _dispose_all_components(self) -> None:
        self._dispose_inference_system()
        self._dispose_validator_runner()
        self._dispose_analyzer()
