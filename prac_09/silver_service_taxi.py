from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagwall of ${self.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagfall
