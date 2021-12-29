class Director:
    def __init__(self):
        self.__builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_system_instance(self):
        variables = self.__builder.set_variables()
        rules = self.__builder.set_rules()
        adi_model = self.__builder.set_adi_model()

        system_instance = self.__builder.set_system_instance(adi_model, variables, rules)
        return system_instance
