proc = int(input("Введите сумму выручки, руб.: "))
cost = int(input("Введите сумму издержек, руб.: "))
profit = proc - cost
#loss = b - a
#rent = a / c

if proc < cost: 
    print("Фирма работает в убыток. Убыток составляет: ", cost - proc, "руб.")
    exit()
if proc == cost:
    print(("Фирма не получила прибыли, но и не понесла убытка"))
    exit()
if proc > cost:
    print("Прибыль составила: ", profit, "руб.")
    effic = proc / profit
    print("Рентабельность фирмы составляет: ", "%.2f" %effic)
    empl = int(input("Введите число сотрудников: "))
    empl_prof = profit / empl
    print("Прибыль на каждого сотрудника составит: ", "%.2f" %empl_prof, "руб.")
    