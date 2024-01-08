import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(2)
page_speed = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 10.0, 1000) / page_speed

x = np.array(page_speed)
y = np.array(purchase_amount)

p_fit = np.poly1d(np.polyfit(x, y, 4))

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p_fit(xp), c='r')
plt.show()