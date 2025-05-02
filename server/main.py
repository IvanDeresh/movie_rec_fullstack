import random
from flask import Flask, request, jsonify
from src.tmdb_api import get_popular_movies, get_movie_details
from src.recommendation_system import recommend_movies
from src.utils import create_movies_dataframe
import os
from dotenv import load_dotenv
from flask_cors import CORS
import logging

load_dotenv()

api_key = os.getenv('API_KEY')

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        movie_title = data.get('title')

        if not movie_title:
            logging.error("title is required")
            return jsonify({'error': 'title is required'}), 400

        popular_movies = get_popular_movies(api_key)

        if not popular_movies:
            logging.error("No popular movies found")
            return jsonify({'error': 'No popular movies found.'}), 404

        movies_df = create_movies_dataframe(popular_movies)

        if movies_df.empty:
            logging.error("Created DataFrame is empty.")
            return jsonify({'error': 'Failed to create DataFrame from popular movies.'}), 500

        matched_movies = movies_df[movies_df['title'].str.lower() == movie_title.lower()]

        if matched_movies.empty:
            logging.warning(f"Movie with title '{movie_title}' not found. Selecting a random movie.")
            selected_movie = movies_df.sample(1).iloc[0]
        else:
            selected_movie = matched_movies.iloc[0]

        movie_id = selected_movie['id']
        logging.info(f"Using movie ID {movie_id} for recommendations.")

        recommendations = recommend_movies(movie_id, movies_df)
        recommended_movies_list = recommendations.to_dict(orient='records')

        return jsonify(recommended_movies_list)

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
