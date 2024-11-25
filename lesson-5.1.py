time_passed = int(input("Введите количество секунд, прошедшего с начала дня: "))

total_seconds_in_day = 24 * 60 * 60
time_remaining = total_seconds_in_day - time_passed
hours = time_remaining // 3600
minutes = (time_remaining % 3600) // 60
seconds = time_remaining % 60
print(f"До полуночи осталось {hours} часов, {minutes} минут и {seconds} секунд.")
