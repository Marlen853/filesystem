# # number = [1,3,4,-5,0,10]
# # even = []
# # odd = []
# # names=["a","b"]
# # if number %2==0:
# #     even.append(number)
# # else:
# #     odd.append(number)








# # 1 Задание

# n = 5
# result = sum(range(1, n + 1))

# print(result)
# # : 15 (1 + 2 + 3 + 4 + 5)







# # 2 Задание

# numbers = list(map(int, input("Введите числа через запятую: ").split(",")))

# even_numbers = [num for num in numbers if num % 2 == 0]
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print("Чётные числа:", even_numbers)
# print("Нечётные числа:", odd_numbers)

# # числа: 1, 2, 3, 4, 5, 6

# # Чётные: [2, 4, 6]
# # Нечётные: [1, 3, 5]












# # 3 Задание
# n = 4
# factorial = math.factorial(n)

# print(factorial)
# # : 24 (4 * 3 * 2 * 1)


# # 4 Задание
# numbers = [15, 22, 8, 19, 31]

# max_num = max(numbers)
# min_num = min(numbers)
# print("Max:", max_num)
# print("Min:", min_num)
# # : Max: 31, Min: 8












# # 5 Задание

# n = 1234
# digit_sum = sum(int(digit) for digit in str(n))

# print(digit_sum)
# # : 10 (1 + 2 + 3 + 4)













# # 6 Задание

# numbers = [3, 5, 3, 7, 6, 5, 3]
# count_dict = Counter(numbers)

# print(count_dict)
# # 3: 3, 5: 2, 7: 1, 6: 1


#  7 Задание
# numbers = [0, 2, 3, 4, 5, 6]
# odd_numbers = [num for num in numbers if num % 2 != 0]

# print(odd_numbers)
# # [3, 5]
















# 8 Задание
# def filter_long_words(words, min_length):
#     return [word for word in words if len(word) > min_length]


# words = ["apple", "kiwi", "banana", "cherry"]
# min_length = 5
# result = filter_long_words(words, min_length)
# print(result)
# # ['apple' 'banana', 'cherry'















# # 9 Задание
# def separate_numbers(numbers):
#     positives = [number for number in numbers if number >= 0]
#     negatives = [number for number in numbers if number < 0]
#     return positives, negatives


# numbers = [-5, 7, 0, -21, 6, -1, 3]
# positives, negatives = separate_numbers(numbers)
# print("Positive numbers:", positives)
# print("Negative numbers:", negatives)


# # : отрицательный: [-5, -21, -1]

# #  положительный: [7, 0, 6, 3]











# # 10 Задание
# def count_long_words(words, n):
#     return sum(1 for word in words if len(word) > n)


# words = ["apple", "banana", "pear", "peach"]
# n = 4
# count = count_long_words(words, n)
# print("Количество слов длиной больше", n, ":", count)
# # : Количество словв 4 : 4
