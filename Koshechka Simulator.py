import random

name = input("Симулятор кошки! Назвите вашу кошку: ")

class koshka:
    def __init__(self, name):
        self.name = name
        self.sila = 100
        self.slipnes = 30
        self.playness = 30
        self.golod = 10
        self.alive = True

    def sleep(self):
        print("спит..."
              "Ваша сила поднялась на 10"
              "Ваша сонливость снизилась на 10"
              "Ваше игривость снизилась на 10"
              "Ваш голод повысился на 8")
        self.sila += 10
        self.slipnes -= 10
        self.playness -= 10
        self.golod += 8

    def play(self):
        print("играет..."
              "Ваша сила снизилась на 7"
              "Ваша сонливость поднялась на 4"
              "Ваш голод поднялся на 8")
        self.sila -= 7
        self.slipnes += 4
        self.golod += 8


    def eat(self):
        print("ест..."
              "Ваша сила повысилась на 15"
              "Ваш голод понизился на 15")
        self.sila += 15
        self.golog -= 15

    def hozgul(self):
        print("гуляет с хозяйном..."
              "Ваша сила снизилась на 10"
              "Ваша сонливость увеличилась на 7"
              "Ваша игривость увеличилась на 10"
              "Ваш голод увеличился на 10")
        self.sila -= 10
        self.slipnes += 7
        self.playness += 10
        self.golod += 10

    def kak(self):
        print("какает..."
              "Ваша сила увеличилась на 3"
              "Ваш голод увеличился на 2")
        self.sila += 3
        self.golod += 2

    def spathoz(self):
        print("спит с хозяйном..."
              "Ваша сила увеличилась на 9"
              "ваша сонливость уменьшилась на 15"
              "Ваш голод увеличился на 8")

    def lazkogt(self):
        print("лазает на когтеточке..."
              "Ваша сила уменьшилась на 10"
              "Ваша сонливость увеличилась на 5"
              "Ваша игривость увеличилась на 10"
              "ваш голод увеличился на 7")
        self.sila -= 10
        self.slipnes += 5
        self.playness += 10
        self.golod += 7

    def alivetest(self):
        if self.sila < 10:
            print("Вы слишком устали, у вас больше нет сил.")
            self.alive = False
        elif self.slipnes >= 60:
            print("Вы слишком устали, у вас больше нет сил бодроствовать.")
            self.alive = False
        elif self.playness < 5:
            print("Вам стало слишком скучно.")
            self.alive = False
        elif self.golod < 1:
            print("Вы сликом голодны.")
            self.alive = False

    def evening(self):
        print("День закончился! Вот ваша статистика за сегодня:")
        print(f"Cила: {self.sila}")
        print(f"{self.slipnes}")
        print(f"{self.playness}")
        print(f"{self.golod}")

    def life(self):

        days = int(0)

        timesday = int(0)

        while timesday < 5:
            rand = random.randint(1,7)

        if rand == 1:
            player_kot.sleep()
            timesday += 1
        elif rand == 2:
            player_kot.play()
            timesday += 1
        elif rand == 3:
            player_kot.eat()
            timesday += 1
        elif rand == 4:
            player_kot.hozgul()
            timesday += 1
        elif rand == 5:
            player_kot.kak()
            timesday += 1
        elif rand == 6:
            player_kot.spathoz()
            timesday += 1
        elif rand == 7:
            player_kot.lazkogt()
            timesday += 1

        if timesday == 5:
            days += 1
            player_kot.evening()
            print(f"Вы уже живёте {days} количество дней.")




player_kot = koshka(name)