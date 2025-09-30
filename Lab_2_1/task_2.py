string= input(" Enter numbers ")

num = string.split()
digits = []
digits = [float(a) if '.' in a else int(a) for a in num]
unique = list(set(digits))
repeated = [a for a in unique if digits.count(a) > 1  ]
even =  [ a for a in digits if isinstance(a, int) and  a % 2 == 0 ]
odd = [a for a in digits if isinstance(a, int) and a % 2 != 0] 
negatives = [a for a  in digits if a < 0 ]
float_dig = [a for a in digits if isinstance(a , float )]
sum_digits_5 = sum(a for a in digits if a % 5 == 0)
max_digit = max(digits)
min_digits = min(digits)
