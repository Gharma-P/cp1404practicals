"""Class that allows to store more than one guitar with its attributes"""
from datetime import date


class Guitar:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(0)
        self.cost = float(0.00)

    def __str__(self):
        return f"Name: {self.name}, Year: {self.year}, Cost: {self.cost:2f}"

    def get_age(self):
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50


