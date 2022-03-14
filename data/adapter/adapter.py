from data.adapter.adaptee import Adaptee
from data.adapter.target import Target
from data.models.adiDuctileIronModel import AdiDuctileIronModel
from data.models.chemicalComposition import ChemicalComposition
from data.models.manufacturingProcess import ManufacturingProcess
from data.models.physicalData import PhysicalData


class Adapter(Target, Adaptee):
    def request(self):
        data = Adapter._load_json_from_file()
        return Adapter._get_adi_ductile_iron_model(data)

    @staticmethod
    def _get_chemical_composition_data(json_data):
        return ChemicalComposition(
            json_data['chemicalComposition']['carbon'],
            json_data['chemicalComposition']['silicon'],
            json_data['chemicalComposition']['magnesium'],
            json_data['chemicalComposition']['sulfur'])

    @staticmethod
    def _get_manufacturing_process_data(json_data):
        return ManufacturingProcess(
            json_data['manufacturingProcess']['austenitizationTemperature'],
            json_data['manufacturingProcess']['austenitizationTime'],
            json_data['manufacturingProcess']['isothermalTransformationTemperature'],
            json_data['manufacturingProcess']['isothermalTransformationTime'])

    @staticmethod
    def _get_physical_data(json_data):
        return PhysicalData(
            json_data['physicalData']['wallThickness'],
            json_data['physicalData']['expectedSpecies'])

    @staticmethod
    def _get_adi_ductile_iron_model(self, json_data):
        chemical_composition = Adapter._get_chemical_composition_data(json_data)
        manufacturing_process = Adapter._get_manufacturing_process_data(json_data)
        physical_data = Adapter._get_physical_data(json_data)
        return AdiDuctileIronModel(chemical_composition, manufacturing_process, physical_data)
