import numpy as np
print("Input expenses (begin with january)")
expenses_month = np.array(list(map(float, input().split())))
if len(expenses_month) != 12:
    print("You have to input 12 month")
else:
    winter_season  = expenses_month[[0,1,11]].sum()
    summer_season = expenses_month[[5,6,7]].sum()
print(f"expenses in winter = {winter_season} ")
print(f"expenses in summer = {summer_season} ")
if winter_season > summer_season:
    print("expenses in winter more than expenses in summer")
elif winter_season == summer_season:
    print("expenses in winter equal expenses in summer")
else: 
    print("expense in summer more than expenses in winter")

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
sorted_indices = np.argsort(expenses_month)[::-1]
print(sorted_indices)
print("months sorted by expenses:")
for i in sorted_indices:
    print(f"{months[i]}({i+1}): {expenses_month[i]}")