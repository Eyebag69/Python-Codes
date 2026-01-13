class Vehicle:
  def __init__(self, brand, model, rent):
    self.brand = brand
    self.model = model
    self.rent = rent
  def calculate_rent(self, days):
    return self.rent * days
class Car(Vehicle):
  def calculate_rent(self, days):
    base = super().calculate_rent(days)
    return base + 300 * days
class Truck(Vehicle):
  def calculate_rent(self, days):
    base = super().calculate_rent(days)
    return base + 500 * days
c = Car("Toyota", "corolla", 1500)
t = Truck("Tata", "LPT", 2500)
print("Car rent:", c.calculate_rent(3))
print("Truck rent", t.calculate_rent(3))
