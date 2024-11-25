# конструкция try-except-finally

# конструкция try-except-else-finally

# try - блок кода, который пытаеться выполниться

# except - блок кода , который выплняеться , если пройзошла ошибка


# 1 Задание

# name = input("ВВедите ваше имя":)
# age = input("введите ваш возраст":)

#  person = {"Имя": name, "лет": age}


# # 2 Задание

#    student_grades = {
#     "Владимир": 12,
#     "Арман": 10,
#     "Нурлан": 11,
#     "Мирас": 9
# }

#   name = input("Введите имя студента: ")

# try:
#     grade = student_grades[name]
#     print(f"Оценка студента {name}: {grade}")
# except KeyError:
#     print("Ошибка: Студент с таким именем не найден.")


# # 3 Задание

# products = {'apple': 50, 'banana': 30, 'orange': 40}

# item = input("Введите название продукта: ").strip().lower()
# price = float(input("Введите новую цену продукта: "))

# products[item] = price
# print("Обновленный словарь:", products)


# #  4 задание
# student_scores = {
#     "Владимир": 85,
#     "Нрулан": 90,
#     "Абылай": 78,
#     "Арман": 88
# }

# name = input("Введите имя студента для удаления: ").strip()

# if name in student_scores:
#     del student_scores[name]
#     print(f"Запись о студенте {name} успешно удалена.")
# else:
#     print("Ошибка: Студент с таким именем не найден.")

# print("Обновленный словарь:", student_scores)


# # 5 Задание

# book_info = {
#     'name': '1984',
#     'author': 'Джордж Оруэлл',
#     'year': 1949
# }

# key = input("Введите ключ для поиска (name, author, year): ").strip()

# value = book_info.get(key, "Ошибка: Ключ не найден.")
# print(value)


# # 6 задание
#  book_info = {"name":
# "1984", "author": "Джордж Оруэлл", "yar": 1949}
#  key = input ("Введите ключ ")
#  value = book_info. get (key)
#  if value:


# print(f"(key): {value}")
#   else:
# print ("Ключ не найден")


# 7 Задание

# user_input = input("Введите число ")

# try:

# number = int(user_input)
# print( "Вы ввели число", number)
#  except ValueError:
# print( "Ошибка")


# 8 Задание

# user_input = input ("Введите число ")
# try:

# number = int(user_input)
#
# print ("Вы ввели число", number)
# except ValueError:
# print ("Ошибка")
# finally:
# print ("Завершение программы")


# #  9 Задание
# user_input = input ("Введите 3 числа через пробел ")
# numbers = user_input.split()
# if len(numbers) |= 3:
# print ("необходимо ввести ровно 3 числа")
# else:
# index = int (input ("Введите индекс"))
# try:
# print (numbers [index])
# except IndexError:
# print("Ошибка индекс выходит за пределы списка")
