from core.builder.base.builder import Builder
from core.inferenceSystems.isothermalTransformationInferenceSystem.isothermalTransformationInferenceSystem import \
    IsothermalTransformationInferenceSystem
from core.inferenceSystems.isothermalTransformationInferenceSystem.isothermalTransformationRules import \
    IsothermalTransformationRulesWrapper
from core.inferenceSystems.isothermalTransformationInferenceSystem.isothermalTransformationVariables import \
    IsothermalTransformationVariableWrapper


class IsothermalTransformationInferenceSystemBuilder(Builder):
    def set_variables(self):
        variables_wrapper = IsothermalTransformationVariableWrapper()
        variables_wrapper.set_variables()

        fuzzy_variables = variables_wrapper.variables
        return fuzzy_variables

    def set_rules(self):
        rules_wrapper = IsothermalTransformationRulesWrapper()
        rules_wrapper.set_rules()

        fuzzy_rules = rules_wrapper.rules
        return fuzzy_rules

    def set_system_instance(self, adi_model, variables, rules):
        return IsothermalTransformationInferenceSystem(adi_model, variables, rules)
