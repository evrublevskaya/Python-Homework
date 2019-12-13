#task_1
var1 = float(input("Введите первое число: ")) 
var2 = float(input("Введите второе число: "))

def div(num_1, num_2):
    try:
        return(num_1 / num_2) 
    except ZeroDivisionError:
        return("Ошибка")

print(div(var1, var2))
    #result = div(var1, var2)
    #print("%.2f" %result) - хотелось бы сделать так при выводе результата, но программа
    #ожидаемо ругнулась на строковый тип при делении на 0. 

#task_2   
def person(name, surname, year, city, e_mail, tel)
inf = f'{name}, {surname}, {year} года рождения, {city}, {e_mail}, {tel}'
return inf
print(Ivan, Petrov, 1991, Dubna, i.petrov@gmail.com, 223-322)

