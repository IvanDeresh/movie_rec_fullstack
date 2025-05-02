import pandas as pd

def create_movies_dataframe(movies):
    df = pd.DataFrame(movies)

    for col in ['title', 'overview', 'tagline', 'release_date', 'genre_ids', 'cast']:
        if col not in df.columns:
            df[col] = ''

    df['combined'] = (
        df['title'].fillna('') + '. ' +
        df['overview'].fillna('') + ' ' +
        df['tagline'].fillna('') + ' ' +
        df['release_date'].fillna('') + ' ' +
        df['genre_ids'].apply(lambda x: ' '.join(map(str, x)) if isinstance(x, list) else '') + ' ' +
        df['cast'].apply(lambda x: ' '.join(x) if isinstance(x, list) else '')
    )

    return df
