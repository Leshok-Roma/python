price = 24.99
minutes = 60
sms = 30
internet = 1024 

u_minutes = int(input("Использовано минут: "))
u_sms = int(input("Использовано SMS: "))
u_internet = int(input("Использовано интернета: "))

e_minutes = max(0, u_minutes - minutes)
e_sms = max(0, u_sms - sms)
e_internet = max(0, u_internet - internet)

e_minutes_pr = e_minutes * 0.89
e_sms_pr = e_sms * 0.59
e_internet_pr= e_internet * 0.79

total_1 = price + e_minutes_pr + e_sms_pr + e_internet_pr
tax = total_1 * 0.02

total = total_1+ tax

print(f"\nБазовая стоимость: {price} руб.")

if e_minutes > 0:
    print(f"Доп. минуты ({e_minutes}): {e_minutes_pr} руб.")
if e_sms > 0:
    print(f"Доп. SMS ({e_sms}): {e_sms_pr} руб.")
if e_internet > 0:
    print(f"Доп. интернет ({e_internet} МБ): {e_internet_pr} руб.")

print(f"Налог (2%): {tax} руб.")
print(f"Итого к оплате: {total} руб.")