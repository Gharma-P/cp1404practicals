"""Testing the taxi class"""

from prac_09.taxi import Taxi

def main():

    test_taxi = Taxi("Prius 1", 100)

    test_taxi.drive(40)

    print(test_taxi)
    print(f"Current Fare: ${test_taxi.get_fare():.2f}")

    test_taxi.start_fare()
    test_taxi.drive(100)

    print(test_taxi)
    print(f"Current Fare: ${test_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()



