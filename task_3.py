p = input(" Введите пароль: ")

if len(p) < 16:
    print("Слишком короткий")
elif p.isalpha() or p.isdigit():
    print("Слабый пароль")
else:
    print("Надежный пароль")