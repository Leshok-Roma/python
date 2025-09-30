print(" Введите любой список ")
lst = list(input().split())
unique_lst = []
list(map(lambda x : unique_lst.append(x) if x not in unique_lst else None, lst))
lst.clear()
lst.extend(unique_lst)
print(lst)