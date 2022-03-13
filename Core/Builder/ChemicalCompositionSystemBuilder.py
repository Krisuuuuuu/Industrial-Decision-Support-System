import Core.Builder.Base.Builder as b
import Core.InferenceSystems.ChemicalCompositionInferenceSystem. \
    ChemicalCompositionVariables as v
import Core.InferenceSystems.ChemicalCompositionInferenceSystem. \
    ChemicalCompositionRules as r
import Core.InferenceSystems.ChemicalCompositionInferenceSystem. \
    ChemicalCompositionInferenceSystem as s


class ChemicalCompositionInferenceSystemBuilder(b.Builder):
    def set_variables(self):
        variables_wrapper = v.ChemicalCompositionVariableWrapper()
        variables_wrapper.set_variables()

        fuzzy_variables = variables_wrapper.get_variables()
        return fuzzy_variables

    def set_rules(self):
        rules_wrapper = r.ChemicalCompositionRulesWrapper()
        rules_wrapper.set_rules()

        fuzzy_rules = rules_wrapper.get_rules()
        return fuzzy_rules

    def set_system_instance(self, adi_model, variables, rules):
        instance = s.ChemicalCompositionInferenceSystem(adi_model, variables, rules)
        return instance
