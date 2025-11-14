import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000 )
y = 5 / (x ** 2 - 9)


y[np.abs(x - 3) < 0.01] = np.nan
y[np.abs(x + 3) < 0.01] = np.nan

plt.figure(figsize=(5,9))
plt.plot(x, y ,label = 'f(x)', color = 'red')
plt.title('chart f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(False)
plt.legend()    
plt.show()