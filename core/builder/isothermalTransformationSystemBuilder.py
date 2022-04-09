from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.variable import FuzzyVariable

from core.builder.base.builder import Builder
from core.inferenceSystems.isothermalTransformationInferenceSystem.isothermalTransformationInferenceSystem import \
    IsothermalTransformationInferenceSystem
from core.inferenceSystems.isothermalTransformationInferenceSystem.isothermalTransformationRules import \
    IsothermalTransformationRulesWrapper
from core.inferenceSystems.isothermalTransformationInferenceSystem.isothermalTransformationVariables import \
    IsothermalTransformationVariableWrapper
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class IsothermalTransformationInferenceSystemBuilder(Builder):
    def set_variables(self) -> dict[str, FuzzyVariable]:
        variables_wrapper: IsothermalTransformationVariableWrapper = IsothermalTransformationVariableWrapper()
        variables_wrapper.set_variables()
        return variables_wrapper.variables

    def set_rules(self) -> list[FuzzyRule]:
        rules_wrapper: IsothermalTransformationRulesWrapper = IsothermalTransformationRulesWrapper()
        rules_wrapper.set_rules()
        return rules_wrapper.rules

    def set_system_instance(self, adi_model: AdiDuctileIronModel, variables: dict[str, FuzzyVariable],
                            rules: list[FuzzyRule]) -> IsothermalTransformationInferenceSystem:
        return IsothermalTransformationInferenceSystem(adi_model, variables, rules)
