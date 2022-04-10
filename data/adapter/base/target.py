from abc import abstractmethod

from data.models.adiDuctileIronModel import AdiDuctileIronModel


class Target:
    @abstractmethod
    def request(self) -> AdiDuctileIronModel: pass
