from Base.Builder import Builder
from ..InferenceSystems.IsothermalTransformationInferenceSystem.IsothermalTransformationVariables \
    import IsothermalTransformationVariableWrapper

from ..InferenceSystems.IsothermalTransformationInferenceSystem.IsothermalTransformationRules \
    import IsothermalTransformationRulesWrapper

from ...IndustrialDecisionSupportSystemData import AdiDuctileIronModel

from ..InferenceSystems.IsothermalTransformationInferenceSystem.IsothermalTransformationInferenceSystem import \
    IsothermalTransformationInferenceSystem


class IsothermalTransformationInferenceSystemBuilder(Builder):
    def set_variables(self):
        variables_wrapper = IsothermalTransformationVariableWrapper()
        variables_wrapper.set_variables()

        fuzzy_variables = variables_wrapper.get_variables()
        return fuzzy_variables

    def set_rules(self):
        rules_wrapper = IsothermalTransformationRulesWrapper()
        rules_wrapper.set_rules()

        fuzzy_rules = rules_wrapper.get_rules()
        return fuzzy_rules

    def set_adi_model(self):
        adi_model = AdiDuctileIronModel(930, 235, 3.60, 2.50, 0.35)
        return adi_model

    def set_system_instance(self, adi_model, variables, rules):
        instance = IsothermalTransformationInferenceSystem(adi_model, variables, rules)
        return instance
