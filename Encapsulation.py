#Darwyn Avila-Medina 
class Vehicle:
    def __init__(self, name, fuel_capacity, cost_per_gallon, mpg):
        self._name = name
        self._fuel_capacity = fuel_capacity
        self._cost_per_gallon = cost_per_gallon
        self._mpg = mpg

    @property
    def range_miles(self):
        return self._fuel_capacity * self._mpg

    @property
    def cost_per_mile(self):
        if self._mpg == 0:
            return float('inf')
        return self._cost_per_gallon / self._mpg

    @property
    def name(self):
        return self._name

v1 = Vehicle("Car", 15, 3.50, 25)
v2 = Vehicle("Motorcycle", 5, 3.50, 50)
v3 = Vehicle("Bus", 80, 3.00, 7)
v4 = Vehicle("Plane", 100, 6.45, 0.5)

vehicles = [v1, v2, v3, v4]

vehicles.sort(key=lambda v: v.cost_per_mile)

print(f"{'Name':<15}{'Range (Miles)':<20}{'Cost/Mile':<15}")
for v in vehicles:
    print(f"{v.name:<15}{v.range_miles:<20.2f}{v.cost_per_mile:<15.4f}")

