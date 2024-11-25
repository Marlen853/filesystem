# кортеж это неизменяемый список
# кортеж - неизмняемая последовательность элементов
large_list = [i for i in range(1, 10_000_000)]
bytes_list = large_list._sizeof
()
kbytes_list = bytes_list // 1024
mbytes_list = kbytes_list // 1024
print()
f = "(bytes_list) байтов, (kbytes_list) киллобайтов, (mbytes_list)занимает список из 10 млн элементов"

# 10 млн элементов
large_tuple = tuple(i for i in range(1, 10_000_000))
bytes_tuple = large_tuple._sizeof
()
kbytes_tuple = bytes_tuple // 1024
mbytes_tuple = kbytes_tuple // 1024
