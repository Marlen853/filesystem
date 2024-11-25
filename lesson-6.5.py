month = int(input("Введите номер месяца (от 1 до 12): "))



season = "Не правильный номер месяца"

if month in [12, 1, 2]:
    season = "Зимма"

elif month in [3, 4, 5]:
    season = "Весна"

elif month in [6, 7, 8]:
    season = "Лето"

elif month in [9, 10, 11]:
    season = "Осень"

print(season)
