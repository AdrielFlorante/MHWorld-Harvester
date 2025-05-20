# Fertilizer.java

class Fertilizer:
    def __init__(self, name, duration, cost, effect):
        self.name = name
        self.duration = duration
        self.cost = cost
        self.effect = effect

    def affects_type(self, crop_type):
        if self.effect == "BoostPlant":
            return crop_type == "Plant"
        elif self.effect == "BoostMushroom":
            return crop_type == "Mushroom"
        elif self.effect == "BoostInsect":
            return crop_type == "Insect"
        else:
            return False  # For effects like Catalyst, etc.

    def __str__(self):
        return self.name

