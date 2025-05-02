from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

def recommend_movies(movie_id, movies_df):
    movie_name = movies_df[movies_df['id'] == movie_id]['title'].values[0]
    print(f"Recommending movies similar to {movie_name}:")

    movie_idx = movies_df[movies_df['id'] == movie_id].index[0]
    combined_text = movies_df['combined'].fillna('').tolist()
    embeddings = model.encode(combined_text, convert_to_tensor=False)

    query_embedding = embeddings[movie_idx]
    cosine_similarities = cosine_similarity([query_embedding], embeddings).flatten()

    movies_df['similarity'] = cosine_similarities
    recommended_movies = movies_df[movies_df['id'] != movie_id].sort_values(by='similarity', ascending=False).head(5)

    return recommended_movies
