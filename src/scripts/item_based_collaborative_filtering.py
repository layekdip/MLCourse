import pandas as pd
import numpy as np

user_data = "D:\\Learning\\PythonLearning\\MLCourse\\src\\data_source\\ml-100k\\u.data"
user_item = "D:\\Learning\\PythonLearning\\MLCourse\\src\\data_source\\ml-100k\\u.item"

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv(user_data, sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv(user_item, sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

print(ratings.head())