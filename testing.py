import numpy as np
import matplotlib.pyplot as plt;

a = []
b = []
z = []

for i in range(100000):
    a.append(np.sqrt(np.random.random()))
    b.append(max(np.random.random(), np.random.random()))
    z = (a[-1] * b[-1])**np.random.random()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4))
ax1.hist(a, 100)
ax2.hist(b, 100)
ax3.hist(z, 100)
plt.show()