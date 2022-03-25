from abc import abstractmethod, ABC

from core.builder.director import Director
from core.inferenceSystems.base.baseInferenceSystem import BaseInferenceSystem
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class AbstractFactory(ABC):
    @abstractmethod
    def create(self) -> BaseInferenceSystem: pass

    def __init__(self, model: AdiDuctileIronModel):
        self._director: Director = Director()
        self._model: AdiDuctileIronModel = model
