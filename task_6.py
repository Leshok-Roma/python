print("Введите значения:")
print("Давление")
p = float(input())
print("Объем")
v = float(input())
print("Температура")
t = float(input())
r= 8.314  

n = (p * v) / (r * t)

print(f"Количество газа: {n} моль")