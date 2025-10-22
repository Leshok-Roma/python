s = input('строка : ').lower()
b = True if s == s[::-1] else False
print('палиндром') if b else print('Не является палиндромом')