# def multiply_elements(lst):#     result = 1
#     for num in lst:#         result *= num
#     return result
# numbers = [2, 3, 4]
# result = multiply_elements(numbers)# print(result)

# # 2# def find_minimum(lst):
#     if not lst:#         return None
#     minimum = lst[0]#     for num in lst[1:]:
#         if num < minimum:#             minimum = num
#     return minimum
# lst = [3, 5, 1, 8, 2]
# print(find_minimum(lst))
# empty_lst = []# print(find_minimum(empty_lst))

# # 3# def num_1(*args):
#     return sum(1 for num in args if is_prime(num))
# def is_prime(num):
#     if num <= 1:#         return False
#     if num == 2 or num == 3:#         return True
#     if num % 2 == 0 or num % 3 == 0:#         return False
#     for i in range(5, int(num**0.5) + 1, 6):#         if num % i == 0 or num % (i + 2) == 0:
#             return False#     return True

# print(num_1(-2, 2, 3, 5, 10))
# # 4# def remove_number(lst, num):
#     count = lst.count(num)#     lst[:] = [x for x in lst if x != num]
#     return count# Rysik = [1, 2, 3, 4, 2, 5, 2, 6]
# removed_count = remove_number(Rysik, 2)# print(removed_count)
# print(Rysik)
# # 5# def merge_lists(list1, list2):
#     return list1 + list2# list1 = [1, 2, 3]
# list2 = [4, 5, 6]# Amogus = merge_lists(list1, list2)
# print(Amogus)
# # 6
