import random
a  = random.randint(1,3)
while True: 
    print("Введите число")
    b = int(input())
    if b == a:
        print("Угадали")
        break
    elif b < a: 
        print("Меньше")
    else :
        print("Больше")