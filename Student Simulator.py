import random

timesday = int(0)

days = int(0)

print("Симулятор студента!")

nam = input("Введите имя студента ")

class student:
    def __init__(self, name):
        self.name = name
        self.happiness = 40
        self.progress = 0
        self.alive = True

    def learn(self):
        print("учится..."
              "Ваше счастье снизилось на 5"
              "Ваш прогресс увеличился на 0.12")
        self.happiness -= 5
        self.progress += 0.12

    def sleep(self):
        print("спит..."
              "Ваше счастье увеличилось на 3")
        self.happiness += 3

    def nich(self):
        print("отдыхает..."
              "Ваше счастье увеличилось на 5"
              "Ваш прогресс снизился на 0.1")
        self.happiness += 5
        self.progress -= 0.1

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

    def life(self,day):

        days = int(0)

        timesday = int(0)

        while timesday < 5:
            rand = random.randint(1,3)

        if rand == 1:
            player_student.learn()
            timesday += 1
        elif rand == 2:
            player_student.sleep()
            timesday += 1
        elif rand == 3:
            player_student.nich()
            timesday += 1
        else:
            pass

        if timesday == 5:
            days += 1
            player_student.vecher()
            print("Вы уже живёте",days,"количество дней")

        else:
            pass


player_student = student(nam)


for day in range(365):
    if player_student.alive == False:
        break

    player_student.life(day)

print("Проигрыш!")