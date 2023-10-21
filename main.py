import time

print("Введите ваш возраст")
vozrast = input()
minimum = int(18)

vozrast = int()

if vozrast >= minimum:
    print("Отлично!")
    time.sleep(2)
    print("Переадресовка...")
else: print("Вы не можете сделать банковскую карту если вам нет 18!")
