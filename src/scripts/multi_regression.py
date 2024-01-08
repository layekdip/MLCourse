import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

input_data_file = "D:\\Learning\\PythonLearning\\MLCourse\\src\\data_source\\cars.xls"

df = pd.read_excel(input_data_file)

df1 = df[['Mileage', 'Price']]
bins = np.arange(0, 50000, 10000)
groups = df1.groupby(pd.cut(df1['Mileage'], bins)).mean()
print(groups.head())
groups['Price'].plot.line()
# plt.show()

scale = StandardScaler()

X = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].values)

X = sm.add_constant(X)

print(X)

est = sm.OLS(y, X).fit()

print(est.summary())

y.groupby(df.Doors).mean()

scaled = scale.transform([[45000, 8, 4]])
scaled = np.insert(scaled[0], 0, 1)  # Need to add that constant column in again.
print(scaled)
predicted = est.predict(scaled)
print(predicted)
