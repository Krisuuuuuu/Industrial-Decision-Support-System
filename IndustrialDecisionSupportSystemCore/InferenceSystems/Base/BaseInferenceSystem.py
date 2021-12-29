from fuzzy_expert.inference import DecompositionalInference


class BaseInferenceSystem:
    def evaluate_results(self): pass

    def __init__(self, adi_model, variables, rules):
        self.__adiModel = adi_model
        self.__fuzzy_variables = variables
        self.__fuzzy_rules = rules
        self.__model = None
        self.__init_model()

    def return_fuzzy_model(self):
        return self.__model

    def return_fuzzy_variables(self):
        return self.__fuzzy_variables

    def return_fuzzy_rules(self):
        return self.__fuzzy_rules

    def __init_model(self):
        self.__model = DecompositionalInference(
            and_operator="min",
            or_operator="max",
            implication_operator="Rc",
            composition_operator="max-min",
            production_link="max",
            defuzzification_operator="cog"
        )
