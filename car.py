from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.__engine = Engine
        self.__battery = Battery

    
    def needs_service(self):
        return self.__engine.NeedsService() or self.__battery.NeedsService()
