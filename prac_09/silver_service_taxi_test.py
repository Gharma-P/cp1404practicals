"""Silver Service Taxi Test"""

from prac_09.silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Limo", 100, 2)
fancy_taxi.drive(18)

fare = fancy_taxi.get_fare()
print(f"Fare for 18km: ${fare:.2f}")

#Assert
assert fare == 48.78, f"Expected fare $48.78 but got ${fare}"