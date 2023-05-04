from Engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, CurrentMileage, LastServiceMileage):
        self.__CurrentMileage = CurrentMileage
        self.__LastServiceMileage = LastServiceMileage

    def NeedsService(self):
        return self.__CurrentMileage - self.__LastServiceMileage > 60000
