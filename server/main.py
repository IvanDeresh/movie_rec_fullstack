import os
from dotenv import load_dotenv
from src.tmdb_api import get_popular_movies, get_movie_details
from src.recommendation_system import recommend_movies
from src.utils import create_movies_dataframe

load_dotenv()

api_key = os.getenv('API_KEY')

if not api_key:
    print("API key not found. Please check your .env file.")
    exit()

def main():
    print("Fetching popular movies...")
    popular_movies = get_popular_movies(api_key)
    
    if popular_movies:
        movies_df = create_movies_dataframe(popular_movies)
        
        movie_id = movies_df.iloc[0]['id']  
        
        recommendations = recommend_movies(movie_id, movies_df)
        print(recommendations)
        
        movie_details = get_movie_details(api_key, movie_id)
        print(f"Details for {movie_details['title']}: {movie_details['overview']}")
    else:
        print("No popular movies found.")

if __name__ == "__main__":
    main()
