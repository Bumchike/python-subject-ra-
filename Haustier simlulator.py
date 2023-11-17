class cat:
    def __init__(self,home):
        self.happiness = 100
        self.len = 10
        self.sitost = 100
        self.uron = 100
        self.home = house()

    def play(self):
        self.happiness += 30
        self.len += 5
        self.sitost -= 20
        self.house.chistota -= 15
        print("Кот поиграл")

    def sleep(self):
        self.happiness += 10
        self.len -= 10
        self.sitost -= 15
        print("Кот поспал")

    def eat(self):
        self.happiness += 20
        self.len += 10
        self.sitost += 30
        self.house.chistota -= 5
        print("Кот поел")

    def battle(self):
        self.happiness -= 20
        self.len += 20
        self.sitost -= 30
        self.house.chistota -= 40
        self.uron -= 40
        print("Кот подрался с собакой!")

class house:
    def __init__(self):
        self.chistota = 100

class dog:
    def __init__(self,home):
        self.happiness = 120
        self.len = 0
        self.sitost = 180
        self.uron = 90
        self.home = house()

    def play(self):
        self.happiness += 40
        self.len += 15
        self.sitost -= 30
        self.house.chistota -= 10
        print("Собака поиграла")

    def sleep(self):
        self.happiness += 5
        self.len -= 10
        self.sitost -= 15
        print("Кот поспал")

    def eat(self):
        self.happiness += 20
        self.len += 10
        self.sitost += 30
        self.house.chistota -= 5
        print("Кот поел")

    def battle(self):
        self.happiness -= 20
        self.len += 20
        self.sitost -= 30
        self.house.chistota -= 40
        self.uron -= 30
        print("Собака подралась с котом!")

