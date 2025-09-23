ip = input("Введите IP-адрес: ")
p = ip.split('.')
v = len(p) == 4

if v:
   
    v= (
        p[0].isdigit() and 0 <= int(p[0]) <= 255 and
        p[1].isdigit() and 0 <= int(p[1]) <= 255 and
        p[2].isdigit() and 0 <= int(p[2]) <= 255 and
        p[3].isdigit() and 0 <= int(p[3]) <= 255
    )

print("Корректный IP-адрес" if v else "Некорректный IP-адрес")