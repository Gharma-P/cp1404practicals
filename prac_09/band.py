"""Band Class"""
from prac_09 import musician


class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        members = ', '.join(str(m) for m in self.musicians)
        return f'{self.name}: {members}'

    def play(self):
        for musician in self.musicians:
            if musician.instruments:
                first_instrument = musician.instruments[0]
                print(f"{musician.name} is playing: {first_instrument}")
            else:
                print(f"{musician.name} needs an instrument")