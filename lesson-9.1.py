# 2 Задание

number = int(input("Введите число: "))

if number % 3 == 0 and number % 5 == 0:
    print("Число делится на 3 и на 5")
elif number % 3 == 0:
    print("Число делится на 3")
elif number % 5 == 0:
    print("Число делится на 5")
else:
    print("Число не делится на 3 и 5")
