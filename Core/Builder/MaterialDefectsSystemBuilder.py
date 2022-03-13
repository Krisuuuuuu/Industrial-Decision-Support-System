import Core.Builder.Base.Builder as b
import Core.InferenceSystems.MaterialDefectsInferenceSystem. \
    MaterialDefectsVariables as v
import Core.InferenceSystems.MaterialDefectsInferenceSystem. \
    MaterialDefectsRules as r
import Core.InferenceSystems.MaterialDefectsInferenceSystem. \
    MaterialDefectsInferenceSystem as s


class MaterialDefectsInferenceSystemBuilder(b.Builder):
    def set_variables(self):
        variables_wrapper = v.MaterialDefectsVariableWrapper()
        variables_wrapper.set_variables()

        fuzzy_variables = variables_wrapper.get_variables()
        return fuzzy_variables

    def set_rules(self):
        rules_wrapper = r.MaterialDefectsRulesWrapper()
        rules_wrapper.set_rules()

        fuzzy_rules = rules_wrapper.get_rules()
        return fuzzy_rules

    def set_system_instance(self, adi_model, variables, rules):
        instance = s.MaterialDefectsInferenceSystem(adi_model, variables, rules)
        return instance
