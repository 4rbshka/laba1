h_age = int(input("Введите возраст человека: "))
if h_age > 21:
    d_age = 2 + (h_age-21)/4
    print("Возраст собаки:", d_age)
elif h_age < 0:
    print("Ошибка: отрицательный возраст")
else:
    d_age = h_age/10.5
    print("Возраст собаки:", d_age)