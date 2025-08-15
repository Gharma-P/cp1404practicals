"""Client code that test nonreliable car vs reliable car"""

from prac_09.unreliable_car import UnreliableCar

def main():

    reliable_car = UnreliableCar("Near New", 100, 90)
    non_reliable_car = UnreliableCar("Old", 100, 30)

    print("Testing reliable car (90%):")
    for i in range(10): # Test 10 times
        distance_driven = reliable_car.drive(10)
        print(f"Run {i+1}: Driven {distance_driven} km, Fuel Left {reliable_car.fuel}")

    print("\nTesting non-reliable car (30%):")
    for i in range(10):
        distance_driven = non_reliable_car.drive(10)
        print(f"Run {i + 1}: Driven {distance_driven} km, Fuel Left {non_reliable_car.fuel}")


if __name__ == "__main__":
    main()







