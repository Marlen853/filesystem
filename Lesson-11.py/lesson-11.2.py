# 1 Задание
text = input("Строка: ")
reversed_text = "".join(reversed(text))
print("перевернутая строка:", reversed_text)


# 2 Задание

text = input("Введите строку: ")

letters_count = sum(c.isalpha() for c in text)
digits_count = sum(c.isdigit() for c in text)

print("Количество букв:", letters_count)
print("Количество цифров:", digits_count)


# 3 Задание

text = input("Введите строку: ")
symbol = input("Введите символ для поиска: ")
count = text.count(symbol)

print(count)


# 4 Задание

text = input("Введите строку: ")
word = input("Введите слово для поиска: ")

count = text.count(word)
print(f"Слово '{word}' встречается {count} раз(а) в строке.")


# 5 Задание

text = input("Введите строку: ")
search_word = input("Введите слово для поиска: ")
replace_word = input("Введите слово для замены: ")

new_text = text.replace(search_word, replace_word)
print("Изменённая строка:", new_text)


# 6 Задания

sports = ("футбол", "Карате", "Муай тай", "Бокс")
if "футбол" in sports:
    print("Футбол есть в списке видов спорта.")
else:
    print("Футбола нет в списке видов спорта.")


# 7 Задание

numbers = (10, 5, 9, 20, 3)
max_value = max(numbers)
min_value = min(numbers)

print("Максимальное знач:", max_value)
print("Минимальное значение:", min_value)


# 8 Задание
number = (1, 2, 3)

temp_list = list(number)

temp_list.append(4)

final_tuple = tuple(temp_list)
print(final_tuple)


# 9 Задание

combined = ("собака", "хомяк", "попугай") + ("гипард", "гиена", "обезьяна")
print(combined)


# 10 Задание
combined = (1, 2, 3) + ("один", "два", "три")
print(combined)
