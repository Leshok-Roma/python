n = int(input("Введите число: "))
if n % 7 == 0:
    print("Магическое число!")
else:
    
    s = sum(map(int, str(abs(n))))
    print(f"Сумма цифр: {s}")