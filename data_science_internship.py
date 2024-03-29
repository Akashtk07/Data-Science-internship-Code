# -*- coding: utf-8 -*-
"""Data Science_Internship.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hr-VtBP9QXWTG2zWjy23MEp8EvYuJQ8M

# **Name**:Akash Tanaji kshirasagar
# **mailID**:aakashkshirsagar2000@gmail.com
# **phone_Num**:7517913910

## **What is the shape of "ratings.csv"?**

# **What is the shape of "movies.csv"**
"""

import pandas as pd
df= pd.read_csv('/content/movies.csv')

df.shape

df1= pd.read_csv('/content/ratings.csv')

df1.shape

"""### How many unique "userId" are available in "ratings.csv"**bold text**"""

df1['userId'].nunique()

"""# Which movie has recieved maximum number of user ratings?


"""

df1['movieId'].value_counts().idxmax()
df[df['movieId'] == 356]

"""# Select all the correct tags submitted by users to "Matrix, The (1999)" movie?"""

df2 =pd.read_csv('/content/tags.csv')

df2[df2['movieId'] == 2571]['tag'].unique()

"""# What is the average user rating for movie named "Terminator 2: Judgment Day (1991)"?"""

df1[df1['movieId'] == 589]['rating'].mean()

"""# How does the data distribution of user ratings for "Fight Club (1999)" movie looks like?"""

import matplotlib.pyplot as plt

# Filter ratings for the movie 'Fight Club (1999)'
fight_club_ratings = df1[df1['movieId'] == 2959]['rating']

# Plot the distribution of user ratings
plt.hist(fight_club_ratings, bins=5, color='skyblue', edgecolor='black')
plt.title('User Ratings Distribution for Fight Club (1999)')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

"""# Which movie is the most popular based on  average user ratings?

"""

# Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings
ratings_grouped = df1.groupby('movieId').agg({'rating': ['count', 'mean']})
ratings_grouped.columns = ['rating_count', 'rating_mean']

# Apply inner join on dataframe created from movies.csv and the grouped df from step 1
merged_df = pd.merge(df, ratings_grouped, on='movieId', how='inner')

# Filter only those movies which have more than 50 user ratings
filtered_df = merged_df[merged_df['rating_count'] > 50]
filtered_df.head()

filtered_df[filtered_df['rating_mean'] == filtered_df['rating_mean'].max()]

"""# Select all the correct options which comes under top 5 popular movies based on number of user ratings."""

filtered_df.nlargest(5, 'rating_count')[['title', 'rating_count', 'rating_mean']]

"""# Which Sci-Fi movie is "third most popular" based on the number of user ratings?"""

filtered_df[filtered_df['genres'].str.contains('Sci-Fi')].nlargest(3, 'rating_count')[['title', 'rating_count', 'rating_mean']]

df3= pd.read_csv('/content/links.csv')

df3.head()

"""# Mention the movieId of the movie which has the highest IMDB rating"""

highest_rating_movie_id = df3.loc[df3['imdbId'].idxmax(), 'movieId']
highest_rating_movie_id

"""# Mention the movieId of the "Sci-Fi" movie which has the highest IMDB rating."""

# Merge the movies and links dataframes on movieId
merged_df = pd.merge(df, df3, on='movieId')

# Filter the merged dataframe for movies with the genre 'Sci-Fi'
scifi_movies = merged_df[merged_df['genres'].str.contains('Sci-Fi', case=False)]

# Display the movie with the highest IMDB rating among the Sci-Fi movies
scifi_movies.loc[scifi_movies['imdbId'].idxmax()]