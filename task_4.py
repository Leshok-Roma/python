import numpy as np
from scipy import integrate

f = lambda x : x**2  * np.sin(x)
res_1, er_1 = integrate.quad(f, 0, np.pi)
print(f" result_1 =  {res_1},  error_1 = {er_1}")

g = lambda x, y : x*y
res_2 ,er_2 = integrate.dblquad(g, 0, 2, lambda x : 0 , lambda x:3  )
print (f' result_2 = {res_2}, error_2 = {er_2}')