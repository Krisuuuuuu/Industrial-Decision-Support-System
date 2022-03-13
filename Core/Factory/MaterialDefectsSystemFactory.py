import Core.Factory.Base.AbstractFactory as af
import Core.Builder.MaterialDefectsSystemBuilder as b


class MaterialDefectsSystemFactory(af.AbstractFactory):
    def __init__(self):
        super().__init__()

    def create(self):
        self._director.set_builder(b.MaterialDefectsInferenceSystemBuilder())
        system_instance = self._director.get_system_instance()

        return  system_instance
