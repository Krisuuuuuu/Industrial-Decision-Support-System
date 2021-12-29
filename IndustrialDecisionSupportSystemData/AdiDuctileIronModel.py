
class AdiDuctileIronModel:
    def __init__(self, austenitizing_temperature, isothermal_transformation_temperature, carbon, silicon, manganese):
        self.austenitizing_temperature = austenitizing_temperature
        self.isothermal_transformation_temperature = isothermal_transformation_temperature
        self.carbon = carbon
        self.silicon = silicon
        self.manganese = manganese
