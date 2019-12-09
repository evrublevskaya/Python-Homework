my_list = list(input("Введите несколько слов через пробел: ").split())
for ind, i in enumerate(my_list, 1):
    print(ind, i[0:10])


