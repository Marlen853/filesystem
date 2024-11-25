# 2 ЗАДАНИЕ

#           0   1   2   3   4
numbers = [10, 20, 30, 40, 50]

index = int(input("Введите индекс для удаления элемента: "))

if 0 <= index < len(numbers):
    del numbers[index]
    print("Элемент удален.")
else:
    print("Не правильный индекс")

print("Обновленный список:", numbers)
