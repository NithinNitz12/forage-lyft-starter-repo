import unittest
from datetime import datetime

from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine

# Service criteria - once every 30,000 miles
class TestCapuletEngine(unittest.TestCase):
    def ShouldBeServiced(self):
        CurrentMileage  = 30001
        LastServiceMileage = 0
        engine = CapuletEngine(CurrentMileage, LastServiceMileage)
        self.assertTrue(engine.NeedsService())

    def ShouldNotBeServiced(self):
        CurrentMileage  = 25000
        LastServiceMileage = 0
        engine = CapuletEngine(CurrentMileage, LastServiceMileage)
        self.assertFalse(engine.NeedsService())

# Service criteria - once every 60,000 miles
class TestWilloughbyEngine(unittest.TestCase):
    def ShouldBeServiced(self):
        CurrentMileage  = 60001
        LastServiceMileage = 0
        engine = WilloughbyEngine(CurrentMileage, LastServiceMileage)
        self.assertTrue(engine.NeedsService())

    def ShouldNotBeServiced(self):
        CurrentMileage  = 55000
        LastServiceMileage = 0
        engine = WilloughbyEngine(CurrentMileage, LastServiceMileage)
        self.assertFalse(engine.NeedsService())

# Service criteria - only when the warning indicator is on
class TestSternmanEngine(unittest.TestCase):
    def ShouldBeServiced(self):
        WarningLightIsOn = True
        engine = SternmanEngine(WarningLightIsOn)
        self.assertTrue(engine.NeedsService())
    
    def ShouldNotBeServiced(self):
        WarningLightIsOn = False
        engine = SternmanEngine(WarningLightIsOn)
        self.assertFalse(engine.NeedsService())