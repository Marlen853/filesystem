# 1 Задание

temperature = float(input("Введите текущую температуру (°C): "))

if temperature < 0:
    outfit = "тёплую куртку и шапку"
elif 0 <= temperature <= 15:
    outfit = "лёгкую куртку"
else:
    outfit = "футболку и шорты"
print(f"При {temperature}°C вам стоит надеть {outfit}.")
