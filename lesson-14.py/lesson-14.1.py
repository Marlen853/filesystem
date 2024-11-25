#  ЧАСТЬ 4


# 1 задание
side_size = int(input("Введите размер квадрата: "))
i = 0
while i < side_size:
    print("*" * side_size)
i += 1


# 2 задание
height = int(input("высота прямоугольника: "))
width = int(input("ширина прямоугольника: "))

while range(height):
    print("*" * width)


# 3 Задание
# Пользователь вводит размер стороны квадрата.

# Спомощью цикла for перебираем все строки от 0 до size 1.


size = int(input("Введите размер стороны квадрата: "))

for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")


# 4 задание
length = int(input(" длину прямоугольника: "))
width = int(input(" ширину прямоугольника: "))

for i in range(length):
    if i == 0 or i == length - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")
