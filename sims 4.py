from random import *

class human:
    def __init__(self,name,work,car,home):
        self.money = 10000
        self.name = name
        self.happiness = 60
        self.nohunger = 80
        self.work = work
        self.car = car
        self.home = home

    def get_home(self):
        self.home = house

    def get_car(self):
        self.car = Auto()

class Auto:
    def __init__(self, brand_list):
        self.brand = choice(list(brand_list))
        self.oil = brand_list[self.brand]["Топливо"]
        self.strong = brand_list[self.brand]["Сила"]
        self.roshod = brand_list[self.brand]["Расход"]

brands_of_car = {
    "BMW":{"Топливо":100, "Сила": 100, "Расход": 6}
    "Ferrari":{"Топливо":80, "Сила": 120, "Расход": 14}
    "Lada":{"Топливо":50, "Сила": 40, "Расход": 10}

}

class house:
    def __init__(self,food,cleaness):
        self.food = 0
        self.cleaness = 0

class job:
    def __init__(self,job,list):
        self.job = 0
        self.gladness = 0
        self.salary = 0

