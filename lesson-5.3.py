price_per_console = float(input("Введите стоимость одной игровой приставки: "))
quantity = int(input("Введите количество приставок: "))
discount = float(input("Введите процент скидки: "))

choice = input(
    "Что вы хотите посчитать? Введите 'общая сумма' или 'стоимость одной': "
).lower()

discounted_price = price_per_console * (1 - discount / 100)

if choice == "общая сумма":
    total_sum = discounted_price * quantity
    print(f"Общая сумма заказа:{total_sum}")
elif choice == "стоимость одной приставки":
    print(f"Стоимость одной приставки с учетом скидки: {discounted_price}")
else:
    print("Неверный ввод. Пожалуйста, введите 'общая сумма' или 'стоимость одной'.")
# примерно number = 3.14159
# print(f"{number:.2f})
