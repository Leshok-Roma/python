print(" Введите строку ")
string = input() 
encoded_str = [] 
count= 1 
previous_char = string[0]
for i in  range(1, len(string)): 
    current_char = string[i]
    if current_char == previous_char : 
        count += 1 
    else :
        encoded_str.append(previous_char + str(count))
        previous_char = current_char
        count = 1
encoded_str.append(previous_char + str(count))
string = ''.join(encoded_str)
print(string)