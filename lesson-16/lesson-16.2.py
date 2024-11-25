# 1 Задание
# def greet(name):
#     print(
#         "Don't let the noise of others' opinions drown out your own inner voice.", name
#     )


# greet("Steve Jobs")


# 2 Задание
# def print_numbers(start, end):
#     for num in range(start + 1, end):
#         if num % 2 != 0:
#             print(num)


# print_numbers(5, 15)


# 3 Задание
# def draw_line(length, direction, symbol):
#     if direction == 'горизонталь':
#         print(symbol * length)

#     elif direction == 'вертикадь':
#         for _ in range(length):
#             print(symbol)

# draw_line(5, 'горизонталь', '*')
# draw_line(3, 'вертикал', '#')


# 4 Задание
# def four(a, b, c, d):

#     return max(a, b, c, d)


# print(four(3, 5, 4, 9))


# 5 задание
# def sum_in_range(start, end):
#     return sum(range(start, end + 1))


# print(sum_in_range(1, 5))
# # 1+2+3+4+5


# 6 Задание
# def is_prime(n):
#     if n <= 1:

#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# print(is_prime(5))
# print(is_prime(6))


# 7 задание
# def is_happy_number(number):
#     num_str = str(number)
#     if len(num_str) != 6:
#         return False
#     first_half = sum(int(num_str[i]) for i in range(3))
#     second_half = sum(int(num_str[i]) for i in range(3, 6))

#     return first_half == second_half


# print(is_happy_number(123420))
# print(is_happy_number(723422))
