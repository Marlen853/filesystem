houre = int(input("Введите время (целjt число от 0 до 23): "))

if 0 <= houre <= 5:
    print("Ночь")
elif 6 <= houre <= 11:
    print("Утро")
elif 12 <= houre <= 18:
    print("День")
elif 18 <= houre <= 23:
    print("Вечр")
else:
    print("Некорректное время. Введите число от 0 до 23.")
