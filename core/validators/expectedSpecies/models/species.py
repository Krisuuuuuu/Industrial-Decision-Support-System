from core.validators.expectedSpecies.models.ductileIronSpeciesEnum import DuctileIronSpecies


class Species:
    def __init__(self, ductile_iron_species: DuctileIronSpecies, min_austenitization_temperature_value: float,
                 max_austenitization_temperature_value: float, min_isothermal_transformation_temperature_value: float,
                 max_isothermal_transformation_temperature_value: float):
        self.ductile_iron_species: DuctileIronSpecies = ductile_iron_species
        self.min_austenitization_temperature_value: float = min_austenitization_temperature_value
        self.max_austenitization_temperature_value: float = max_austenitization_temperature_value
        self.min_isothermal_transformation_temperature_value: float = min_isothermal_transformation_temperature_value
        self.max_isothermal_transformation_temperature_value: float = max_isothermal_transformation_temperature_value
