def person(name, surname, year, city, e_mail, tel):
    inf = f'{name} {surname}, {year} года рождения, {city}, e-mail: {e_mail}, тел.: {tel}'
    return inf
print(person("Иван", "Петров", 1991, "Дубна", "i.petrov@gmail.com", "223-322"))