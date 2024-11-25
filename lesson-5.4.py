file_size_gb = float(input("Введите размер файла в гигабайтах: "))
internet_speed_bps = float(
    input("Введите скорость интернет-соединения в битах в секунду: ")
)

file_size_bits = file_size_gb * (10**9)
choice = input(
    "За сколько времени вы хотите узнать скачивание? Введите 'часы', 'минуты' и 'секунды': "
).lower()

download_time_seconds = file_size_bits / internet_speed_bps

if choice == "секунды":
    print(f"Файл скачивается за {download_time_seconds} секунд.")
elif choice == "минуты":
    download_time_minutes = download_time_seconds / 60
    print(f"Файл скачивается за {download_time_minutes} минут.")
elif choice == "часы":
    download_time_hours = download_time_seconds / 3600
    print(f"Файл скачивается за {download_time_hours} часов.")
else:
    print("Неверный ввод. Пожалуйста, введите 'часы', 'минуты' или 'секунды'.")
    5 + 5
