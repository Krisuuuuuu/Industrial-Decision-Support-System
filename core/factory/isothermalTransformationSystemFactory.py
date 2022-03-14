import core.factory.base.abstractFactory as af
import core.builder.isothermalTransformationSystemBuilder as b


class IsothermalTransformationSystemFactory(af.AbstractFactory):
    def __init__(self):
        super().__init__()

    def create(self):
        self._director.set_builder(b.IsothermalTransformationInferenceSystemBuilder())
        system_instance = self._director.get_system_instance()

        return system_instance
