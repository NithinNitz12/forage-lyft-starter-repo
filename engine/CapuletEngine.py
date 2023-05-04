from Engine import Engine

class CapuletEngine(Engine):
    def __init__(self, CurrentMileage, LastServiceMileage):
        self.__CurrentMileage = CurrentMileage
        self.__LastServiceMileage = LastServiceMileage

    def NeedsService(self):
        return self.CurrentMileage - self.LastServiceMileage > 30000
