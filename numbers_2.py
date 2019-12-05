a = int(input("Введите число: "))

if a <= 0:
    print("Число должно быть больше 0")
    exit()

max = 0


while a > 0:
    if a % 10 > max:
        max = a % 10
    a = a // 10
    

print("Максимальная цифра - %d" %max)