# def greet():
#     print("я функция")


# greet()


# def greet(name):
#     print(f"Спасиьо что обратились к нам;\n\n рады оказать вам наши услуги,{name}")
#     greet("Arman")
#     greet("Almas")
#     greet("nursultan")


# def is_even(number):
#     if number % 2 == 0:
#         print("Четные")
#     else:
#         print("нечет")


# is_even(2)
# is_even(3)
# is_even(5)
# is_even(6)




# def is_even(number:int)->bool:
#     return number % 2 == 0
# is_even(4)
# is_even(5)
# is_even(6)
# is_even(7)
# print(is_even(4))
# print(is_even(5))
# print(is_even(6))
# print(is_even(7))





grades = [12, 10, 8, 12, 9, 10, 6, 8, 4]


def average(number: list[int]) -> float:
    return sum(number) / len(number)

print(f"Моя средння оценка:{average(grades)}")
