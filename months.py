
month = int(input("Введите месяц в виде числа: "))
months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

if month == months_list[11] or month == months_list[0] or month == months_list[1]:
        print("Зима")
elif month == months_list[2] or month == months_list[3] or month == months_list[4]:
        print("Весна")
elif month == months_list[7] or month == months_list[6] or month == months_list[7]:
        print("Лето")
elif month == months_list[8] or month == months_list[9] or month == months_list[10]:
        print("Осень")
     


month = int(input("Введите месяц в виде числа: "))
my_dict = { "dec" : 12, "jan" : 1, "feb" : 2, "mar" : 3, "apr" : 4, "may" : 5, "june" : 6, "july" : 7, "aug" : 8, "sept" : 9, "oct" : 10, "nov" : 11 }
if month == my_dict["dec"] or month == my_dict["jan"] or month == my_dict["feb"]:
    print("Зима")
elif month == my_dict["mar"] or month == my_dict["apr"] or month == my_dict["may"]:
    print("Весна")
elif month == my_dict["june"] or month == my_dict["july"] or month == my_dict["aug"]:
    print("Лето")
elif month == my_dict["sept"] or month == my_dict["oct"] or month == my_dict["nov"]:
        print("Осень")

