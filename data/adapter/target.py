from abc import abstractmethod


class Target:
    def __init__(self):
        self._adi_ductile_iron_model = None

    @abstractmethod
    def request(self): pass

    def _get_model(self):
        return self._adi_ductile_iron_model
