import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30,color="red")
plt.title("Histogram")
plt.xlabel("Wartości")
plt.ylabel("Częstość")

plt.savefig('wykres.png')
plt.savefig('wykres.pdf')
plt.show()
