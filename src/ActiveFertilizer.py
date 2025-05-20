# ActiveFertilizer.java

class ActiveFertilizer:
    def __init__(self, fertilizer, remaining_duration):
        self.fertilizer = fertilizer
        self.remaining_duration = remaining_duration

    def copy(self):
        return ActiveFertilizer(self.fertilizer, self.remaining_duration)

    def __str__(self):
        return f"{self.fertilizer.name} ({self.remaining_duration})"

