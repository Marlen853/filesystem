# k = 18
# while k % 2 == 0:
#     k //= 2

# #  1 интерация
# # 18
# # 9


# x = 16
# while x != 9:
#     x -= 1


number = 43

while True:
     guess = int(input("Попробуй угадать число в диапазоне от 1 до 50":)):
     if number == guess:
        print(f"молодец! ты угадал. задданое число было: {number}")
        break
     else:
        print("нет! попробуй еще раз")
 