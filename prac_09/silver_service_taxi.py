"""Silver Service taxi class, premium service charged"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Silver service taxi class is charged at a different rate"""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        return super().get_fare() + SilverServiceTaxi.flag_fall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flag_fall:.2f}"


