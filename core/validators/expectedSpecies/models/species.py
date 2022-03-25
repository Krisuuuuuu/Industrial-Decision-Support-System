
class Species:
    def __init__(self, ductile_iron_species, min_austenitization_temperature_value,
                 max_austenitization_temperature_value, min_isothermal_transformation_temperature_value,
                 max_isothermal_transformation_temperature_value):
        self.ductile_iron_species = ductile_iron_species
        self.min_austenitization_temperature_value = min_austenitization_temperature_value
        self.max_austenitization_temperature_value = max_austenitization_temperature_value
        self.min_isothermal_transformation_temperature_value = min_isothermal_transformation_temperature_value
        self.max_isothermal_transformation_temperature_value = max_isothermal_transformation_temperature_value


