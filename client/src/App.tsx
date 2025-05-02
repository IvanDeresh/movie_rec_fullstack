import React, { useState } from "react";
import { Movie, RecommendationResponse } from "./types/fetch";

function App() {
  const [movieTitle, setMovieTitle] = useState<string>("");
  const [recommendations, setRecommendations] = useState<
    RecommendationResponse[]
  >([]);
  const [error, setError] = useState<string>("");

  const handleSearch = async () => {
    setError("");
    setRecommendations([]);
    if (!movieTitle) {
      setError("Please enter a movie ID");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/recommend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title: movieTitle }),
      });

      if (response.ok) {
        const data: RecommendationResponse[] = await response.json();
        setRecommendations(data);
      } else {
        const data = await response.json();
        setError(data.error || "Error occurred");
      }
    } catch (err: any) {
      setError("Server error: " + err.message);
    }
  };

  return (
    <div className="App">
      <h1>Movie Recommendation System</h1>
      <input
        type="text"
        value={movieTitle}
        onChange={(e) => setMovieTitle(e.target.value)}
        placeholder="Enter movie ID"
      />
      <button onClick={handleSearch}>Search</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {recommendations.length > 0 && (
        <div>
          <h2>Recommended Movies:</h2>
          <ul>
            {recommendations.map((movie) => (
              <li key={movie.id}>
                <strong>{movie.title}</strong>: {movie.overview}
                <p>Similarity: {movie.similarity}</p>
                <img
                  src={`https://image.tmdb.org/t/p/w500${movie.backdrop_path}`}
                  alt={movie.title}
                  style={{ width: "200px" }}
                />
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
