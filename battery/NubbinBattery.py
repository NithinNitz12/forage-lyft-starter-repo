from battery import Battery

class NubbinBattery(Battery):
    def __init__(self, LastServiceDate, CurrentDate):
        self.__LastServiceDate = LastServiceDate
        self.__CurrentDate = CurrentDate

    def NeedsService(self):
        return (self.__CurrentDate - self.__LastServiceDate) >= 4