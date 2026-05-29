import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 400)

y = np.sqrt(x**3 - x + 1)

plt.plot(x, y)
plt.plot(x, -y)

plt.title("Curba Eliptica")
plt.grid(True)
plt.show()