ip = input("Введите IP-адрес: ")
parts_of_ip = ip.split('.')
print(parts_of_ip)
correct  = len(parts_of_ip) == 4
if correct:
   
    correct= (
        parts_of_ip[0].isdigit() and 0 <= int(parts_of_ip[0]) <= 255 and
        parts_of_ip[1].isdigit() and 0 <= int(parts_of_ip[1]) <= 255 and
        parts_of_ip[2].isdigit() and 0 <= int(parts_of_ip[2]) <= 255 and
        parts_of_ip[3].isdigit() and 0 <= int(parts_of_ip[3]) <= 255
    )

print("Корректный IP-адрес" if correct else "Некорректный IP-адрес")