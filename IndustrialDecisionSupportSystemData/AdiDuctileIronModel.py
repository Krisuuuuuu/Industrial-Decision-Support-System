
class AdiDuctileIronModel:
    def __init__(self, defects_quantity, defects_size, austenitizing_temperature, isothermal_transformation_temperature,
                 carbon, silicon, manganese):
        self.defects_quantity = defects_quantity
        self.defects_size = defects_size
        self.austenitizing_temperature = austenitizing_temperature
        self.isothermal_transformation_temperature = isothermal_transformation_temperature
        self.carbon = carbon
        self.silicon = silicon
        self.manganese = manganese
