class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        info = f"{self.year} {self.brand} {self.model}"
        print(info)

car1 = Car("Ford", "Mustang", 2022)
car2 = Car("Chevrolet", "Camaro", 2021)

car1.display_info()
car2.display_info()
