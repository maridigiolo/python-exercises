class Vehicle:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)

car = Vehicle('Audi', 'Q5', '2013')
print(car.make, car.model, car.year)

car.print_info()
