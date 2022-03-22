from core.builder.base.builder import Builder
from core.inferenceSystems.austenitizationProcessInferenceSystem.austenitizationProcessInferenceSystem import \
    AustenitizationProcessInferenceSystem
from core.inferenceSystems.austenitizationProcessInferenceSystem.austenitizationProcessRules import \
    AustenitizationProcessRulesWrapper
from core.inferenceSystems.austenitizationProcessInferenceSystem.austenitizationProcessVariables import \
    AustenitizationProcessVariableWrapper


class AustenitizationProcessInferenceSystemBuilder(Builder):
    def set_variables(self):
        variables_wrapper = AustenitizationProcessVariableWrapper()
        variables_wrapper.set_variables()

        fuzzy_variables = variables_wrapper.variables
        return fuzzy_variables

    def set_rules(self):
        rules_wrapper = AustenitizationProcessRulesWrapper()
        rules_wrapper.set_rules()

        fuzzy_rules = rules_wrapper.rules
        return fuzzy_rules

    def set_system_instance(self, adi_model, variables, rules):
        return AustenitizationProcessInferenceSystem(adi_model, variables, rules)