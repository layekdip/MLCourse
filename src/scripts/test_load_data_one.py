import pandas as pd
import matplotlib.pyplot as plt

input_data_file = "D:\\Learning\\PythonLearning\\MLCourse\\src\\data_source\\PastHires.csv"
print(input_data_file)

df = pd.read_csv(input_data_file)
# print(df.head(10))
print(df.shape)
print(df.size)
print(len(df))
print(df.columns)

degree_count = df['Level of Education'].value_counts()
degree_count.plot(kind='bar')
plt.show()
