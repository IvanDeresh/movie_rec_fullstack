import React, { useState } from "react";
import { Movie, RecommendationResponse } from "./types/fetch";
import RecomendationItem from "./components/RecomendationItem";

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
    <div className="flex items-center  pt-20 flex-col min-w-[100vw] h-full">
      <h1 className="text-[2rem]">Movie Recommendation System</h1>
      <div className="flex justify-between gap-4">
        <input
          type="text"
          value={movieTitle}
          onChange={(e) => setMovieTitle(e.target.value)}
          placeholder="Enter movie ID"
          className="border border-[#1a1a1a] rounded-md pl-2"
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {recommendations.length > 0 && (
        <div className="flex flex-col justify-center">
          <h2 className="text-center font-bold text-xl py-5">
            Recommended Movies:
          </h2>
          <ul className="flex flex-col items-center gap-3">
            {recommendations.map((movie) => (
              <RecomendationItem {...movie} />
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
