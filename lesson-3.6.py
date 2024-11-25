# 1задание
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for number in range(start, end + 1):
    if number % 7 == 0:
        print(number)


# 2 Задание
start = int(input("начало диапазона: "))
end = int(input("конец диапазона: "))

print("Все числа диапазона:")
for number in range(start, end + 1):
    print(number, end=" ")
print("\n")

print("Числа в возрастающем порядке:")
for number in sorted(range(start, end + 1)):
    print(number, end=" ")
print("\n")

print("Числа, кратные 7:")
for number in range(start, end + 1):
    if number % 7 == 0:
        print(number, end=" ")
print("\n")
count_multiples_of_5 = sum(1 for number in range(start, end + 1) if number % 5 == 0)
print("Количество чисел, кратных 5:", count_multiples_of_5)


# 3 Задание
start = int(input("Введите начало диапазона: "))
end = int(input("Введитеконец диапазона: "))

for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# 1 Задание
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0
sum_multiple_9 = 0
count_multiple_9 = 0

for number in range(start, end + 1):
    if number % 2 == 0:
        sum_even += number
        count_even += 1
    else:
        sum_odd += number
        count_odd += 1
    if number % 9 == 0:
        sum_multiple_9 += number
        count_multiple_9 += 1
average_even = sum_even / count_even if count_even != 0 else 0
average_odd = sum_odd / count_odd if count_odd != 0 else 0
average_multiple_9 = sum_multiple_9 / count_multiple_9 if count_multiple_9 != 0 else 0

print("Сумма четных чисел:", sum_even)
print("Среднее четных чисел:", average_even)
print("Сумма нечетных чисел:", sum_odd)
print("Среднее нечетных чисел:", average_odd)
print("Сумма чисел, кратных 9:", sum_multiple_9)
print("Среднее чисел, кратных 9:", average_multiple_9)


# 2 Задание
length = int(input("Введите длину линии: "))
symbol = input("Введите символ для заполнения линии: ")

for _ in range(length):
    print(symbol)


# 3 Задание
while True:
    number = int(input("число: "))

    if number == 7:
        print("Good bye")
        break
    elif number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")


# 4 Задание
total_sum = 0
while True:
    number = int(input("Введите число: "))

    if number == 7:
        print("Good bye")
        break
    total_sum += number
    print("Текущая сумма:", total_sum)
