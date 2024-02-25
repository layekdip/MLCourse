import pandas as pd

input_data_file = "D:\\Learning\\PythonLearning\\MLCourse\\src\\data_source\\all_banks"
df = pd.read_pickle(input_data_file)

print(df.head())

