from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.variable import FuzzyVariable

from core.builder.base.builder import Builder
from core.inferenceSystems.chemicalCompositionInferenceSystem.chemicalCompositionInferenceSystem import \
    ChemicalCompositionInferenceSystem
from core.inferenceSystems.chemicalCompositionInferenceSystem.chemicalCompositionRules import \
    ChemicalCompositionRulesWrapper
from core.inferenceSystems.chemicalCompositionInferenceSystem.chemicalCompositionVariables import \
    ChemicalCompositionVariableWrapper
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class ChemicalCompositionInferenceSystemBuilder(Builder):
    def set_variables(self) -> dict[str, FuzzyVariable]:
        variables_wrapper: ChemicalCompositionVariableWrapper = ChemicalCompositionVariableWrapper()
        variables_wrapper.set_variables()
        return variables_wrapper.variables

    def set_rules(self) -> list[FuzzyRule]:
        rules_wrapper: ChemicalCompositionRulesWrapper = ChemicalCompositionRulesWrapper()
        rules_wrapper.set_rules()
        return rules_wrapper.rules

    def set_system_instance(self, adi_model: AdiDuctileIronModel, variables: dict[str, FuzzyVariable],
                            rules: list[FuzzyRule]) -> ChemicalCompositionInferenceSystem:
        return ChemicalCompositionInferenceSystem(adi_model, variables, rules)
