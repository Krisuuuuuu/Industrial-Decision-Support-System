class ManufacturingProcess:
    def __init__(self, austenitization_time: float,
                 austenitization_temperature: float,
                 isothermal_transformation_time: float,
                 isothermal_transformation_temperature: float):
        self.austenitization_time: float = austenitization_time
        self.austenitization_temperature: float = austenitization_temperature
        self.isothermal_transformation_time: float = isothermal_transformation_time
        self.isothermal_transformation_temperature: float = isothermal_transformation_temperature
