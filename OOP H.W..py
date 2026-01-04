"""
PART A
"""


# 1. Vehicle class without variables or methods
class Vehicle:
    pass


# 2. Vehicle class with instance attributes max_speed and mileage
class Vehicle:
    # 4. Class attribute for default color
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    # 5. Seating capacity method
    def seating_capacity(self, capacity=4):
        """Display seating capacity of the vehicle"""
        print(f"Seating capacity: {capacity}")

    # 6. Fare method
    def fare(self, capacity=4):
        """Calculate fare as capacity * 100"""
        total_fare = capacity * 100
        print(f"Fare: {total_fare}")
        return total_fare


# 3. Bus class inheriting Vehicle
class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        # Inherit parent constructor
        super().__init__(max_speed, mileage)

    # Override seating_capacity with default 50
    def seating_capacity(self, capacity=50):
        print(f"Bus seating capacity: {capacity}")

    # Override fare to add extra 50
    def fare(self, capacity=50):
        total_fare = super().fare(capacity) + 50
        print(f"Bus fare with extra charges: {total_fare}")
        return total_fare


# Example usage
if __name__ == "__main__":
    # Create a vehicle
    v1 = Vehicle(120, 15000)
    print(f"Vehicle color: {v1.color}, Max Speed: {v1.max_speed}, Mileage: {v1.mileage}")
    v1.seating_capacity()
    v1.fare()

    print("\n")

    # Create a bus
    bus1 = Bus(80, 30000)
    print(f"Bus color: {bus1.color}, Max Speed: {bus1.max_speed}, Mileage: {bus1.mileage}")
    bus1.seating_capacity()
    bus1.fare()
