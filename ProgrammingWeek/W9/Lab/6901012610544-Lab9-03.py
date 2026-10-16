#====================================================
#|                                                  |
#|       6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ        |
#|                                                 |
#===================================================

class Vehicle:
    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate: str = license_plate
        self.brand: str = brand
        self.model: str = model
        self.year: str = year
        self.daily_rate: float = daily_rate

    def show_info(self):
        print(f"License Plate: {self.license_plate}\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nDaily Rate: {self.daily_rate} thb.")

    def calculate_rental_cost(self, days: int):
        return f"Rental Cost: {self.daily_rate * days}"

class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, seat):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seat: int = seat

    def show_info(self):
        super().show_info()
        print(f"Seat: {self.seat}")

    def calculate_rental_cost(self, days):
            charged_days = (days // 7) * 5 + min(days % 7, 5)
            return f"Rental Cost: {self.daily_rate * charged_days}"
    
class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload: float = payload

    def show_info(self):
        super().show_info()
        print(f"Payload: {self.payload} Kg")


if __name__ == "__main__":
    vehicle1 = Vehicle("วร5705", "Toyota", "Tiger", "2544", 1000)
    car1 = Car("วร5705", "Toyota", "Tiger", "2544", 1000, 6)
    truck1 = Truck("วร5705", "Toyota", "Tiger", "2544", 1000, 5000)

    vehicle1.show_info()
    car1.show_info()
    print(car1.calculate_rental_cost(7))
    truck1.show_info()
    print(truck1.calculate_rental_cost(7))