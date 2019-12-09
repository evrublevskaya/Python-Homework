#my_list = (input("Введите любые данные через пробел: ").split())
#my_list[1::2], my_list[:-1:2] = my_list[:-1:2], my_list[1::2]
#print(my_list)



my_list = (input("Введите любые данные через пробел: ").split())
if len(my_list) % 2 == 0:
    length = len(my_list)
else:
    length = len(my_list) - 1

for i in range(0, length, 2):
    n = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = n

print(my_list)
