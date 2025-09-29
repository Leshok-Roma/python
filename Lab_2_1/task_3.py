digits = input(" Enter numbers ").split()
digits =  list(map(float, digits))
digits.sort() 
print(digits)
second = digits[-2]
print(second)
    
