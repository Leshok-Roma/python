d = int(input("Введите день рождения: "))
m = int(input("Введите месяц рождения: "))


if (m == 3 and d>= 21) or (m == 4 and d <= 19):
    print("Овен")
elif (m == 4 and d >= 20) or (m == 5 and d <= 20):
    print("Телец")
elif (m == 5 and d >= 21) or (m == 6 and d <= 20):
    print("Близнецы")
elif (m == 6 and d >= 21) or (m == 7 and d <= 22):
    print("Рак")
elif (m == 7 and d >= 23) or (m== 8 and d <= 22):
    print("Лев")
elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
    print("Дева")
elif (m == 9 and d >= 23) or (m == 10 and d   <= 22):
    print("Весы")
elif (m == 10 and d >= 23) or (m == 11 and d <= 21):
    print("Скорпион")
elif (m == 11 and d >= 22) or (m == 12 and d <= 21):
    print("Стрелец")
elif (m == 12 and d >= 22) or (m == 1 and d <= 19):
    print("Козерог")
elif (m == 1 and d >= 20) or (m == 2 and d <= 18):
    print("Водолей")
else:
    print("Рыбы")