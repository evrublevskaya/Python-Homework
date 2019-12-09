my_list = [9, 6, 6, 5, 4, 1]
num = int(input("Введите число: "))

print(my_list)

if num > 9:
    my_list.insert(0, num)
    print(my_list)
    exit()
elif num == 1:
    my_list.append(num)
    print(my_list)
    exit()

i = 0

if num in my_list:
    while i < len(my_list):
        if num == my_list[i] and i + 1 != len(my_list) and my_list[i + 1] != my_list[i]:
            my_list.insert(i + 1, num)
            break
        i += 1
else:
    while i < len(my_list):
        if my_list[i + 1] < num:
            my_list.insert(i + 1, num)
            break
        i += 1

print(my_list)


