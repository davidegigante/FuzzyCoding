import numpy as np

class FuzzyVariable(object):

    def __init__(self, var_name: str, var_range: list, unit: str = None):
        self.name = var_name
        self.range = var_range
        self.unit = unit
    
    def __str__(self):
        start, end = self.range
        return f'{self.name} ({self.unit}) - Defined on ({start}, {end})' if self.unit is not None else f'{self.name} - Defined on ({start}, {end})'
    
print(FuzzyVariable('temperature', [-273.5, np.inf]))
print(FuzzyVariable('temperature', [-273.5, np.inf], unit='K'))