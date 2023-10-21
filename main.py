import time

print("Введите ваш возраст")
vozrast = input(int)

vozrast = int(vozrast)
minimum = int(18)

if vozrast >= minimum:
    print("Отлично!")
    time.sleep(2)
    print("Переадресовка...")
else:
    print("Вы не можете сделать банковскую карту если вам нет 18!")
    time.sleep(2)
    print("Переадресовка...")
