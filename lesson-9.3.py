# 4 Задание

speed = float(input("Введите скорость интернета (в Мбит/с): "))
if speed < 10:
    print("Очень медленная сеть")
elif speed <= 50:
    print("Средняя скорость сети")
else:
    print("Высокая скорость сети")
