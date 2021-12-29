class BaseVariableWrapper:
    def __init__(self):
        self.__fuzzy_variables = None

    def set_variables(self): pass

    def get_variables(self):
        return self.__fuzzy_variables
