input_seconds = int(input("Введите количество секунд: "))

minutes = input_seconds // 60
seconds = input_seconds % 60

print(f"{input_seconds} секунд - {minutes} минут {seconds} секунд")