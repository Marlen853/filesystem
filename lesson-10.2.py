# 1 задание
text = input("Hello world: ")

reversed_string = text[::-1]
print(reversed_string)


# 2 Задание
changed_case = text.swapcase()

print(changed_case)


# 3 Задание
text = input("Введите строку: ")
substring = input("Введите подстроку: ")
position = text.find(substring)
if position != -1:
    print(position)
else:
    print("подстрока не нашлась.")


# 4 Задание
user = input("введите строкуу: ")

contains_python = "python" in user

print(contains_python)


# 5 Задание
user = input("Введите строку: ")
char = input("Введите символ: ")

print(user.count(char))


# 6 Задание
user = input("Введите строку: ")

palindrome = user == user[::-1]
print("Строка является палиндромом." if palindrome else "Строка не является.")


# 7 Задание
text = input("Введите строку: ")

old_char = input("Введите символ для замены: ")
new_char = input("Введите новый символ: ")

print(text.replace(old_char, new_char))


# 8 Задание
string1 = input(" Введите первую строку: ")
string2 = input("Введите вторую строку: ")

print(string1 == string2)


# 9 Задание
user = input("Вводим строку: ")

is_alpha = user.isalpha()
print(is_alpha)


# 10 Задание
user = input(" Вводим строку: ")

print(user.isalnum())


# 11 Задание
string1 = input(" первоя строку: ")
string2 = input(" вторая строку: ")

if len(string1) > len(string2):
    print(f"Первая строка длиннее: {string1}', вторая короче: '{string2}'")

elif len(string1) < len(string2):
    print(f"Вторая строка длиннее: '{string2}', первая короче: '{string1}'")

else:
    print("Обе строки одинаковой длины.")
