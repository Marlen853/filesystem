import math


diameter = float(input("Введите диаметр окружности: "))
choice = input("Что вы хотите посчитать? Введите 'периметр' или 'площадь': ").lower()

if choice == "периметр":
    perimeter = math.pi * diameter
    print(f"Периметр окружности: {perimeter}")
elif choice == "площадь":
    radius = diameter / 2
    area = math.pi * (radius**2)
    print(f"Площадь окружности: {area}")
else:
    print("Неверный ввод. Пожалуйста, введите 'периметр' или 'площадь'.")
