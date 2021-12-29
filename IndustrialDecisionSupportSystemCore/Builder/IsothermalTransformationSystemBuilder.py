import IndustrialDecisionSupportSystemCore.Builder.Base.Builder as b
import IndustrialDecisionSupportSystemCore.InferenceSystems.IsothermalTransformationInferenceSystem. \
    IsothermalTransformationVariables as v
import IndustrialDecisionSupportSystemCore.InferenceSystems.IsothermalTransformationInferenceSystem. \
    IsothermalTransformationRules as r
import IndustrialDecisionSupportSystemData.AdiDuctileIronModel as m
import IndustrialDecisionSupportSystemCore.InferenceSystems.IsothermalTransformationInferenceSystem. \
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

    def set_adi_model(self):
        adi_model = m.AdiDuctileIronModel(930, 235, 3.60, 2.50, 0.35)
        return adi_model

    def set_system_instance(self, adi_model, variables, rules):
        instance = s.IsothermalTransformationInferenceSystem(adi_model, variables, rules)
        return instance
