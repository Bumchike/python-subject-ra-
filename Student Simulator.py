# Учитывайте что тут есть дз и это всё!!!!!!!!!
import random

timesday = int(0)

days = int(0)

print("Симулятор студента! Ваша цель закончить уник. Для этого вам надо прожить целый год или же получить 5 очков прогресса.")

nam = input("Введите имя студента ")

class student:
    def __init__(self, name):
        self.name = name
        self.happiness = 40
        self.progress = 0.4
        self.money = 100
        self.learning = 70
        self.alive = True

    def learn(self):
        print("учится..."
              "Ваше счастье снизилось на 5"
              "Ваш прогресс увеличился на 0.12"
              "Ваша учёба поднялась на 10")
        self.happiness -= 5
        self.progress += 0.12
        self.learning += 10

    def sleep(self):
        print("спит..."
              "Ваше счастье увеличилось на 2"
              "Ваша учёба снизилась на 3")
        self.happiness += 2
        self.learning -= 3

    def nich(self):
        print("отдыхает..."
              "Ваше счастье увеличилось на 5"
              "Ваш прогресс снизился на 0.1"
              "Ваше количество денег снизилось на 10"
              "Ваша учёба снизилась на 5")
        self.happiness += 5
        self.progress -= 0.1
        self.money -= 10
        self.learning -= 5

    def work(self):
        print("работает..."
              "Ваше счастье снизилось на 0.4"
              "Ваш прогресс увеличился на 0.1"
              "Ваша учёба снизилась на 1")
        self.happiness -= 0.4
        self.progress += 0.1
        self.learning -= 1

    def vecher(self):
        print("День закончился! вот ваша статистика за сегодня:")
        print(f"Счастье: {self.happiness}")
        print(f"Прогресс: {self.progress}")

    def alivetest(self):

        if self.happiness < 0:
            print("Плохо тебе. Ты устал от универа и сам отчислился")
            self.alive = False

        elif self.progress < 0.3:
            print("Гений мыслей, тебя отчислили!")
            self.alive = False

        elif self.progress > 5:
            print("Победа! Ты успешно закончил универ!")
            self.alive = False

        elif self.money < 5:
            print("У тебя нет денег и тебе нечего кушать ")
            self.alive = False



    def life(self,day):

        days = int(0)

        timesday = int(0)

        while timesday < 5:
            rand = random.randint(1,4)

        if rand == 1:
            player_student.learn()
            timesday += 1
        elif rand == 2:
            player_student.sleep()
            timesday += 1
        elif rand == 3:
            player_student.nich()
            timesday += 1
        elif rand == 4:
            player_student.work()
            timesday += 1

        if timesday == 5:
            days += 1
            player_student.vecher()
            print("Вы уже живёте",days,"количество дней")

        else:
            pass

        if self.money < 50:
            print("Иди работай!")
        else:
            pass

        if self.learning < 10:
            print("Иди учись!")


player_student = student(nam)


for day in range(365):
    if player_student.alive == False:
        break

    player_student.life(day)

print("Игра закончена!")