#  1 задание
# salaries = [30000, 40000, 50000, 60000, 60000, 70000]
# salaries = [salary * 1.1 for salary in salaries]


#  2 задание
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [num for num in numbers if num % 2 == 0]

#  3 задание
# names = ["Владимир", "Нурлан", "Марлен", "Алуа"]
# capitalized_names = [name for name in names if name[0].isupper()]

#  4 задание
# passwords = ["qwerty123", "secur", "helloWorld", "qwerty123!", "12345"]
# strong_passwords = [
#     pwd
#     for pwd in passwords
#     if any(c.isdigit() for c in pwd) and any(c.isupper() for c in pwd)
# ]

#  5 задание
# lines = ["Hello", "", "World", "Python", ""]
# non_empty_lines = [line for line in lines if line]

#  6 задание
# ages = [15, 22, 18, 24, 30, 17, 21]
# adults = [age for age in ages if age >= 18]

#  7 задание
# numbers = [5, 10, 25, 30, 45, 50]
# divisible_by_five = [num for num in numbers if num % 5 == 0]

#  8 задние
# prices = [250, 350, 400, 150, 200, 500, 100]
# discounted_prices = [price - 100 for price in prices if price - 100 < 300]

#  9 задание
# words = ["apple", "banana", "cherry", "potato", "watermellon", "grape"]
# filtered_words = [word.upper() for word in words if word[0] in "ab"]

#  10 задание
# students = [
#     {"name": "Vladimir", "grade": 85},
#     {"name": "Abylay", "grade": 70},
#     {"name": "Alua", "grade": 65},
#     {"name": "Nurlan", "grade": 90},
# ]
# average_grade = sum(student["grade"] for student in students) / len(students)
# top_students = [student for student in students if student["grade"] > average_grade]
