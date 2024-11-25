# ЧАСТЬ 3


# 1 Задание
# number = int(input("Введите число: "))

# for i in range(1, 4):
#     print(f"{number * i}", end=" ")


# 2 задание
# rates = {"USD": 1, "KZT": 420}

# while True:
#     print("\nmenu:")
#     print("1. Конвертировать из долларов в тенге")
#     print("2. Конвертировать из тенге в доллары")
#     print("3. exit")

#     choice = input("Введите номер действия: ")

#     if choice == "1":
#         amount = float(input("Введите сумму в долларах: "))
#         result = amount * rates["KZT"]
#         print(f"{amount} USD = {result:.2f} KZT")

#     elif choice == "2":
#         amount = float(input("Введите сумму в тенге: "))
#         result = amount / rates["KZT"]
#         print(f"{amount} KZT = {result:.2f} USD")

#     elif choice == "3":
#         break

#     else:
#         print("Некорректный выбор.")


# # 3 задание
# lower = int(input(" нижния граница диапазона: "))  # границы 1 и 7, а gjnjv число 4.

# upper = int(input("верхнея граница диапозона: "))

# while True:
#     number = int(input(f"Введите число в диапазоне от {lower} до {upper}: "))
#     if lower <= number <= upper:
#         break
#     print("Число не попадает в диапазон. Попробуйте снова.")

# for i in range(lower, upper + 1):
#     if i == number:
#         print(f"!{i}!", end=" ")
#     else:
#         print(i, end=" ")


# # 4 задание
# import random
# import time

# # напиштие число от 1 до 500
# secret_num = random.randint(1, 500)
# attempts = 0

# print("Угадайте число от 1 до 500! Введите 0, чтобы выйти.")

# start_time = time.time()

# while True:
#     guess = int(input("Ваше число: "))

#     if guess == 0:
#         print("Вы вышли из игры.")
#         break


#     attempts += 1
#     if guess < secret_num:
#         print("Слишком мало!")
#     elif guess > secret_num:
#         print("Слишком много!")
#     else:
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         print(f"Поздравляем! Вы угадали число {secret_num} за {attempts} попыток.")
#         print(f"Время игры: {elapsed_time:.2f} секунд.")
#         break
