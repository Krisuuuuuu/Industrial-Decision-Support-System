import core.factory.base.abstractFactory as af
import core.builder.isothermalTransformationSystemBuilder as b


class IsothermalTransformationSystemFactory(af.AbstractFactory):
    def __init__(self, model):
        super().__init__(model)

    def create(self):
        self._director.set_builder(b.IsothermalTransformationInferenceSystemBuilder())
        system_instance = self._director.get_system_instance(self._model)

        return system_instance
