"""Class inherited from Car"""
import random
from car import Car


class UnreliableCar(Car):
    """A car that only sometimes drive based on reliability %"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
