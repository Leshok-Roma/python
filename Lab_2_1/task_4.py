lst1 = input(" Enter numbers ").split()
lst1 =  list(map(float, lst1))

lst2 = input(" Enter numbers ").split()
lst2 =  list(map(float, lst2))

union= [a for a in lst1 if a in lst2 ]
lst1_without_lst2 = [a for a in lst1 if a not in lst2 ]
not_union = [a for a in lst1 + lst2 if a not in union ]

print(union)
print(lst1_without_lst2 )   
print(not_union)