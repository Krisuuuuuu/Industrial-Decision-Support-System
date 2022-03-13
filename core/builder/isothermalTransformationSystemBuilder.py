import core.builder.base.builder as b
import core.inferenceSystems.isothermalTransformationInferenceSystem. \
    isothermalTransformationVariables as v
import core.inferenceSystems.isothermalTransformationInferenceSystem. \
    isothermalTransformationRules as r
import core.inferenceSystems.isothermalTransformationInferenceSystem. \
    isothermalTransformationInferenceSystem as s


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
