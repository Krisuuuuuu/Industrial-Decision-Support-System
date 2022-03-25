from data.models.chemicalComposition import ChemicalComposition
from data.models.manufacturingProcess import ManufacturingProcess
from data.models.physicalData import PhysicalData


class AdiDuctileIronModel:
    def __init__(self,
                 chemical_composition: ChemicalComposition,
                 manufacturing_process: ManufacturingProcess,
                 physical_data: PhysicalData):
        self.chemical_composition: ChemicalComposition = chemical_composition
        self.manufacturing_process: ManufacturingProcess = manufacturing_process
        self.physical_data: PhysicalData = physical_data
