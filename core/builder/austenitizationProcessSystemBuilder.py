from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.variable import FuzzyVariable

from core.builder.base.builder import Builder
from core.inferenceSystems.austenitizationProcessInferenceSystem.austenitizationProcessInferenceSystem import \
    AustenitizationProcessInferenceSystem
from core.inferenceSystems.austenitizationProcessInferenceSystem.austenitizationProcessRules import \
    AustenitizationProcessRulesWrapper
from core.inferenceSystems.austenitizationProcessInferenceSystem.austenitizationProcessVariables import \
    AustenitizationProcessVariableWrapper
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class AustenitizationProcessInferenceSystemBuilder(Builder):
    def set_variables(self) -> dict[str, FuzzyVariable]:
        variables_wrapper: AustenitizationProcessVariableWrapper = AustenitizationProcessVariableWrapper()
        variables_wrapper.set_variables()
        return variables_wrapper.variables

    def set_rules(self) -> list[FuzzyRule]:
        rules_wrapper: AustenitizationProcessRulesWrapper = AustenitizationProcessRulesWrapper()
        rules_wrapper.set_rules()
        return rules_wrapper.rules

    def set_system_instance(self, adi_model: AdiDuctileIronModel, variables: dict[str, FuzzyVariable],
                            rules: list[FuzzyRule]) -> AustenitizationProcessInferenceSystem:
        return AustenitizationProcessInferenceSystem(adi_model, variables, rules)
