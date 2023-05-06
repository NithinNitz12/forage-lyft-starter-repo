from Tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, SensorData):
        self.__SensorData = list(SensorData)
    
    def NeedsService(self):
        for x in range(4):
            if self.__SensorData[x] >= 3.0:
                return True
            else:
                return False