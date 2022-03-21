from core.builder.base.builder import Builder
from core.inferenceSystems.chemicalCompositionInferenceSystem.chemicalCompositionInferenceSystem import \
    ChemicalCompositionInferenceSystem
from core.inferenceSystems.chemicalCompositionInferenceSystem.chemicalCompositionRules import \
    ChemicalCompositionRulesWrapper
from core.inferenceSystems.chemicalCompositionInferenceSystem.chemicalCompositionVariables import \
    ChemicalCompositionVariableWrapper


class ChemicalCompositionInferenceSystemBuilder(Builder):
    def set_variables(self):
        variables_wrapper = ChemicalCompositionVariableWrapper()
        variables_wrapper.set_variables()

        fuzzy_variables = variables_wrapper.variables
        return fuzzy_variables

    def set_rules(self):
        rules_wrapper = ChemicalCompositionRulesWrapper()
        rules_wrapper.set_rules()

        fuzzy_rules = rules_wrapper.rules
        return fuzzy_rules

    def set_system_instance(self, adi_model, variables, rules):
        return ChemicalCompositionInferenceSystem(adi_model, variables, rules)
