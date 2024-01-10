import pandas as pd
import numpy as np

user_data = "D:\\Learning\\PythonLearning\\MLCourse\\src\\data_source\\ml-100k\\u.data"
user_item = "D:\\Learning\\PythonLearning\\MLCourse\\src\\data_source\\ml-100k\\u.item"

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv(user_data, sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")
# ratings = pd.read_csv(user_data, sep='\t')

m_cols = ['movie_id', 'title']
movies = pd.read_csv(user_item, sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
# movies = pd.read_csv(user_item, sep='|')

ratings = pd.merge(movies, ratings)
print(ratings.head())

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(movieRatings.head())

starWarsRatings = movieRatings['Star Wars (1977)']
print(starWarsRatings.head())

similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
print(df.head(10))

similarMovies.sort_values(ascending=False)

movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
print(movieStats.head())

popularMovies = movieStats['rating']['size'] >= 100
print(movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15])

#df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))

# Updated for newer Pandas releases that don't allow merging between different levels; we must flatten it first now.
mappedColumnsMoviestat=movieStats[popularMovies]
mappedColumnsMoviestat.columns=[f'{i}|{j}' if j != '' else f'{i}' for i,j in mappedColumnsMoviestat.columns]
df = mappedColumnsMoviestat.join(pd.DataFrame(similarMovies, columns=['similarity']))
print(df.sort_values(['similarity'], ascending=False)[:15])
