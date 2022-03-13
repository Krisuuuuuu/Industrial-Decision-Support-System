from Data.Adapter.Adaptee import Adaptee
from Data.Adapter.Target import Target
from Data.Models.AdiDuctileIronModel import AdiDuctileIronModel
from Data.Models.ChemicalComposition import ChemicalComposition
from Data.Models.ManufacturingProcess import ManufacturingProcess
from Data.Models.PhysicalData import PhysicalData


class Adapter(Target, Adaptee):
    def request(self):
        data = self._load_json_from_file()
        self.adi_ductile_iron_model = self._get_adi_ductile_iron_model(data)
        return self.adi_ductile_iron_model

    def _get_chemical_composition_data(self, json_data):
        return ChemicalComposition(
            json_data['chemicalComposition']['carbon'],
            json_data['chemicalComposition']['silicon'],
            json_data['chemicalComposition']['magnesium'],
            json_data['chemicalComposition']['sulfur'])

    def _get_manufacturing_process_data(self, json_data):
        return ManufacturingProcess(
            json_data['manufacturingProcess']['austenitizationTemperature'],
            json_data['manufacturingProcess']['austenitizationTime'],
            json_data['manufacturingProcess']['isothermalTransformationTemperature'],
            json_data['manufacturingProcess']['isothermalTransformationTime'])

    def _get_physical_data(self, json_data):
        return PhysicalData(
            json_data['physicalData']['wallThickness'],
            json_data['physicalData']['expectedSpecies'])

    def _get_adi_ductile_iron_model(self, json_data):
        chemical_composition = self._get_chemical_composition_data(json_data)
        manufacturing_process = self._get_manufacturing_process_data(json_data)
        physical_data = self._get_physical_data(json_data)
        return AdiDuctileIronModel(chemical_composition, manufacturing_process, physical_data)
