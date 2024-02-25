import matplotlib.pyplot as plt

# fig = plt.figure()
# axis1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axis2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

fig, axis = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))
x = [1, 2, 3, 4]
y = [7, 8, 9, 10]

for current_ac in axis:
    current_ac.plot(x, y, label="Testing")
    current_ac.legend()
plt.tight_layout()

fig.savefig('my_plot.jpg')
plt.show()
