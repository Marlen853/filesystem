num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))


print("Выберите операцию:")
print("1 - Сумма")
print("2 - Разница")
print("3 - Среднее арифметическое")
print("4 - Произведение")
choice = input("Введите номер операции: ")


if choice == "1":
    result = num1 + num2
    print(f"Сумма: {result}")
elif choice == "2":
    result = num1 - num2
    print(f"Разница: {result}")
elif choice == "3":
    result = (num1 + num2) / 2
    print(f"Среднее арифметическое: {result}")
elif choice == "4":
    result = num1 * num2
    print(f"Произведение: {result}")
else:
    print("Неверный выбор операции")
