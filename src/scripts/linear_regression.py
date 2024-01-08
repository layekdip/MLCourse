import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

page_speed = np.random.normal(3.0, 1.0, 1000)
purchase_amount = 100 - (page_speed + np.random.normal(0, 0.1, 1000) * 3)

slope, intercept, r_value, p_value, std_err = stats.linregress(page_speed, purchase_amount)

print(r_value ** 2)


def predict(x):
    return slope * x + intercept


# plt.scatter(page_speed, purchase_amount)
# plt.show()

fit_line = predict(page_speed)
plt.scatter(page_speed, purchase_amount)
plt.plot(page_speed, fit_line, c='r')
plt.show()
