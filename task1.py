import numpy as np
import matplotlib.pyplot as plt

x_deg = np.linspace(-360,360, 360)
x_rad = np.radians(x_deg)

f = np.exp(np.cos(x_rad)) + np.log(np.cos(0.6 * x_rad) ** 2 + 1) * np.sin(x_rad)
h = -np.log((np.cos(x_rad) + np.sin(x_rad)) ** 2 + 2.5) + 10

plt.figure(figsize=(5,10))    
plt.plot(x_deg, f, label='f(x)')
plt.plot(x_deg, h, label = 'h(x)')
plt.title('charts f(x) and h(x)')
plt.xlabel('x, deg')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()