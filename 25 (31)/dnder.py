
class Factory:
    def __init__(self, name, open_year):
        self.name = name
        self.open_year = open_year
        self.cars = []


class Car:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if args:
            for arg in args:
                if isinstance(arg, cars):
                    self.cars.append(args)



kia = Factory("Kia", 2500000, 2023) 
kia