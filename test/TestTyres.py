import unittest

from tyre.CarriganTyre import CarriganTyre
from tyre.OctoprimeTyre import OctoprimeTyre

class TestCarriganTyre(unittest.TestCase):
    def ShouldBeServiced(self):
        SensorData = [0.9, 0.1, 0.2, 0.3]
        tyre = CarriganTyre(SensorData)
        self.assertTrue(tyre.NeedsService())

    def ShouldNotBeServiced(self):
        SensorData = [0.5, 0.1, 0.2, 0.3]
        tyre = CarriganTyre(SensorData)
        self.assertFalse(tyre.NeedsService())

class TestOctoprimeTyre(unittest.TestCase):
    def ShouldBeServiced(self):
        SensorData = [0.8, 0.8, 0.8, 0.7]
        tyre = OctoprimeTyre(SensorData)
        self.assertTrue(tyre.NeedsService())

    def ShouldNotBeServiced(self):
        SensorData = [0.1, 0.2, 0.4, 0.2]
        tyre = OctoprimeTyre(SensorData)
        self.assertFalse(tyre.NeedsService())