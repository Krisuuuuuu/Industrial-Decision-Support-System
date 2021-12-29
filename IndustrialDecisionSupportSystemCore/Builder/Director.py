class Director:
    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    def get_system_instance(self):
        variables = self._builder.set_variables()
        rules = self._builder.set_rules()
        adi_model = self._builder.set_adi_model()

        system_instance = self._builder.set_system_instance(adi_model, variables, rules)
        return system_instance
