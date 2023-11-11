
class human:
    def __init__(self,name):
        self.name = name

class Bus:
    def __init__(self,brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self,human):
        self.passenger.append(human)

    def print_passengers_name(self):
        if self.passenger != []:
            print(f"Бренд автобуса: {self.brand} Пассажиры:")

            for passenger in self.passenger:
                print(passenger.name)

        else:
            print(f"Нет пасажиров в {self.brand}")



dan = human("Дэн")
max = human("Макс")

car = Bus("BMW")

car.add_passenger(dan)
car.add_passenger(max)
car.print_passengers_name()