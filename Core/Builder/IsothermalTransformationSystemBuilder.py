import Core.Builder.Base.Builder as b
import Core.InferenceSystems.IsothermalTransformationInferenceSystem. \
    IsothermalTransformationVariables as v
import Core.InferenceSystems.IsothermalTransformationInferenceSystem. \
    IsothermalTransformationRules as r
import Core.InferenceSystems.IsothermalTransformationInferenceSystem. \
    IsothermalTransformationInferenceSystem as s


class IsothermalTransformationInferenceSystemBuilder(b.Builder):
    def set_variables(self):
        variables_wrapper = v.IsothermalTransformationVariableWrapper()
        variables_wrapper.set_variables()

        fuzzy_variables = variables_wrapper.get_variables()
        return fuzzy_variables

    def set_rules(self):
        rules_wrapper = r.IsothermalTransformationRulesWrapper()
        rules_wrapper.set_rules()

        fuzzy_rules = rules_wrapper.get_rules()
        return fuzzy_rules

    def set_system_instance(self, adi_model, variables, rules):
        return s.IsothermalTransformationInferenceSystem(adi_model, variables, rules)
