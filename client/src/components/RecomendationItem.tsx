import React, { FC } from "react";
import { RecommendationResponse } from "../types/fetch";

const RecomendationItem: FC<RecommendationResponse> = ({
  id,
  title,
  overview,
  backdrop_path,
  vote_average,
  similarity,
}) => {
  return (
    <li
      key={id}
      className="bg-white rounded-2xl w-[50%] shadow-md p-4 flex flex-col md:flex-row gap-4 transition hover:shadow-lg"
    >
      <img
        src={`https://image.tmdb.org/t/p/w500${backdrop_path}`}
        alt={title}
        className="rounded-xl w-full md:w-60 h-auto object-cover"
      />

      <div className="flex flex-col justify-between">
        <div>
          <h3 className="text-xl text-gray-800 font-semibold mb-2">{title}</h3>
          <p className="text-gray-600 text-sm mb-3">{overview}</p>
        </div>

        <div className="flex items-center justify-between text-sm text-gray-700">
          <span className="font-medium">
            🎯 Similarity:{" "}
            <span className="text-blue-600">
              {(Number(similarity.toFixed(2)) * 100).toFixed(0)}%
            </span>
          </span>
          <span>⭐ {vote_average.toFixed(1)}/10</span>
        </div>
      </div>
    </li>
  );
};

export default RecomendationItem;
