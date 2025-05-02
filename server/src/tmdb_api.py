import requests

def get_popular_movies(api_key, pages=50):
    all_movies = []
    for page in range(1, pages + 1):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page={page}'
        response = requests.get(url)
        if response.status_code == 200:
            all_movies.extend(response.json()['results'])
        else:
            print(f"Error fetching page {page}: {response.status_code}")
            break
    return all_movies

def get_movie_details(api_key, movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
