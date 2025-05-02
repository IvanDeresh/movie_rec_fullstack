from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def recommend_movies(movie_id, movies_df):
    movie_name = movies_df[movies_df['id'] == movie_id]['title'].values[0]
    print(f"Recommending movies similar to {movie_name}:")

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['overview'].fillna(''))

    movie_idx = movies_df[movies_df['id'] == movie_id].index[0]

    cosine_similarities = cosine_similarity(tfidf_matrix[movie_idx], tfidf_matrix).flatten()

    movies_df['similarity'] = cosine_similarities

    recommended_movies = movies_df[movies_df['id'] != movie_id].sort_values(by='similarity', ascending=False).head(5)

    return recommended_movies
