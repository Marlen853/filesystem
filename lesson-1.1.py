# 1 Задание


# seconds_passed = int(input("Введите количество секунд, прошедших с начала дня: "))

# total_seconds_in_a_day = 86400  # 24 * 60 * 60

# seconds_remaining = total_seconds_in_a_day - seconds_passed

# hours_remaining = seconds_remaining // 3600
# minutes_remaining = (seconds_remaining % 3600) // 60
# seconds_remaining = seconds_remaining % 60

# print(f"До полуночи осталось: {hours_remaining} часов, {minutes_remaining} минут, {seconds_remaining} секунд.")


# 2 задание

# import math

# diameter = float(input("Введите диаметр окружности: "))
# radius = diameter / 2

# choice = input("Введите 'п' для периметра или 's' для площади: ").strip().lower()

# if choice == 'п':
#     perimeter = math.pi * diameter
#     print("Периметр окружности:", perimeter)
# elif choice == 's':
#     area = math.pi * (radius ** 2)
#     print("Площадь окружности:", area)
# else:
#     print("Некорректный выбор.")


# 3 задание

# price_per_console = float(input("Введите стоимость одной игровой приставки: "))

# quantity = int(input("Введите количество приставок: "))

# discount_percentage = float(input("Введите процент скидки: "))

# choice = input("Введите 'с' для общей суммы заказа или 'д' для стоимости одной приставки с учетом скидки: ").strip().lower()

# if choice == 'с':
#     total_cost = price_per_console * quantity
#     print("Общая сумма заказа:", total_cost)
# elif choice == 'д':
#     discount_amount = price_per_console * (discount_percentage / 100)
#     discounted_price = price_per_console - discount_amount
#     print("Стоимость одной приставки с учетом скидки:", discounted_price)
# else:
#     print("Некорректный выбор.")


# 4 задание.


# file_size_gb = float(input("Введите размер файла в гигабайтах: "))

# internet_speed_bps = float(input("Введите скорость интернет-соединения в битах в секунду: "))

# file_size_bits = file_size_gb * 8 * 10**9

# download_time_seconds = file_size_bits / internet_speed_bps
# choice = input("Введите 'ч' для времени в часах, 'м' для минут или 'с' для секунд: ").strip().lower()

# if choice == 'ч':
#     download_time_hours = download_time_seconds / 3600
#     print("Время скачивания файла:", download_time_hours, "часов")
# elif choice == 'м':
#     download_time_minutes = download_time_seconds / 60
#     print("Время скачивания файла:", download_time_minutes, "минут")
# elif choice == 'с':
#     print("Время скачивания файла:", download_time_seconds, "секунд")
# else:
#     print("Некорректный выбор.")


# # 5 Задание

# hours = int(input("Введите количество часов (0-23): "))
# if 0 <= hours < 6:
#     print("Good Night")
# elif 6 <= hours < 13:
#     print("Good Morning")
# elif 13 <= hours < 17:
#     print("Good Day")
# elif 17 <= hours < 24:
#     print("Good Evening")
# else:
#     print("Некорректный ввод. Часы должны быть в диапазоне от 0 до 23.")
