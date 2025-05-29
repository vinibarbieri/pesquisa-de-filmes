from typing import List
from app.models.movie import Movie
from app.repositories.file_movie_repository import FileMovieRepository

class MovieService:
    def __init__(self, movie_repository: FileMovieRepository):
        self.movie_repository = movie_repository
        self._movies_cache = None

    def _load_movies_if_needed(self) -> List[Movie]:
        if self._movies_cache is None:
            self._movies_cache = self.movie_repository.load_movies()
        return self._movies_cache

    def get_all_movies(self) -> List[Movie]:
        return self._load_movies_if_needed()

    def search_movies(self, name_query: str = "", genre_query: str = "", date_query: str = "") -> List[Movie]:
        # Obtém a lista completa de filmes
        filtered_movies = self._load_movies_if_needed()

        # Remove espaços em branco e converte para minúsculas as queries
        name_query = name_query.strip().lower()
        genre_query = genre_query.strip().lower()
        date_query = date_query.strip()

        # Filtra por nome
        if name_query:
            filtered_movies = [
                movie for movie in filtered_movies
                if name_query in movie.title.lower()
            ]

        # Filtra por gênero
        if genre_query:
            filtered_movies = [
                movie for movie in filtered_movies
                if genre_query in movie.genre.lower()
            ]

        # Filtra por data de lançamento
        if date_query:
            filtered_movies = [
                movie for movie in filtered_movies
                if date_query in movie.release_date
            ]

        return filtered_movies 