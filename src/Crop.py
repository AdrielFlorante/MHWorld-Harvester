# Crop.java

from copy import deepcopy

class Crop:
    def __init__(self, name, base_growth_time, base_yield, crop_type):
        self.name = name
        self.base_growth_time = base_growth_time
        self.base_yield = base_yield
        self.type = crop_type
        self.current_growth = 0
        self.yield_amount = 0
        self.active_fertilizers = []

    def copy(self):
        clone = Crop(self.name, self.base_growth_time, self.base_yield, self.type)
        clone.current_growth = self.current_growth
        clone.yield_amount = self.yield_amount
        clone.active_fertilizers = [af.copy() for af in self.active_fertilizers]
        return clone

