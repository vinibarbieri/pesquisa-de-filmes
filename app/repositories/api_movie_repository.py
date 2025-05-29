import requests
from typing import List, Optional, Dict
from app.models.movie import Movie

class ApiMovieRepository:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"
        self.image_base_url = "https://image.tmdb.org/t/p/w500"
        self.genre_map = self._load_genre_map()

    def _load_genre_map(self) -> Dict[int, str]:
        try:
            response_data = self._make_request("/genre/movie/list")
            if not response_data or "genres" not in response_data:
                print("Aviso: Não foi possível carregar o mapa de gêneros do TMDb")
                return {}
            
            return {genre["id"]: genre["name"] for genre in response_data["genres"]}
        except Exception as e:
            print(f"Erro ao carregar mapa de gêneros: {str(e)}")
            return {}

    def _make_request(self, endpoint: str, params: Optional[dict] = None) -> Optional[dict]:
        try:
            full_url = f"{self.base_url}{endpoint}"
            request_params = params.copy() if params else {}
            request_params["api_key"] = self.api_key
            
            response = requests.get(full_url, params=request_params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error making request to TMDb API: {str(e)}")
            return None

    def _parse_movie_data(self, api_movie_dict: dict) -> Movie:
        # Process genre_ids into a comma-separated string of genre names
        genre_ids = api_movie_dict.get("genre_ids", [])
        genre_names = []
        
        for genre_id in genre_ids:
            if genre_id in self.genre_map:
                genre_names.append(self.genre_map[genre_id])
        
        genre = ", ".join(genre_names) if genre_names else "Gênero não informado"

        return Movie(
            title=api_movie_dict.get("title", ""),
            genre=genre,
            release_date=api_movie_dict.get("release_date", ""),
            overview=api_movie_dict.get("overview"),
            poster_path=api_movie_dict.get("poster_path"),
            tmdb_id=api_movie_dict.get("id")
        )

    def get_popular_movies(self, page: int = 1) -> List[Movie]:
        response_data = self._make_request("/movie/popular", {"page": page})
        if not response_data or "results" not in response_data:
            return []
        
        return [self._parse_movie_data(movie) for movie in response_data["results"]]

    def search_movies_by_name(self, name_query: str, page: int = 1) -> List[Movie]:
        response_data = self._make_request(
            "/search/movie",
            {"query": name_query, "page": page}
        )
        if not response_data or "results" not in response_data:
            return []
        
        return [self._parse_movie_data(movie) for movie in response_data["results"]] 