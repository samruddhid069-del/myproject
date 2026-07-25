class Car:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity
        self.total = price * quantity


cars = [
    Car("Toyota", "Innova", 2000000, 2),
    Car("Honda", "City", 1500000, 6),
    Car("Hyundai", "Creta", 1800000, 1),
    Car("Tata", "Nexon", 1200000, 7),
    Car("Mahindra", "XUV700", 2500000, 3)
]

print("Cars with quantity LESS than 5:")
for car in cars:
    if car.quantity < 5:
        print(car.brand, car.model, "- Qty:", car.quantity)

print("\nCars with quantity GREATER than 5:")
for car in cars:
    if car.quantity > 5:
        print(car.brand, car.model, "- Qty:", car.quantity)