export interface Movie {
  id: number;
  title: string;
  adult: boolean;
  backdrop_path: string;
  genre_ids: number[];
  overview: string;
  vote_average: number;
  vote_count: number;
  similarity?: number;
}

export interface RecommendationResponse {
  id: number;
  title: string;
  overview: string;
  backdrop_path: string;
  vote_average: number;
  similarity: number;
}
