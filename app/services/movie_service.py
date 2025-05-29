from typing import List
from app.models.movie import Movie
from app.repositories.api_movie_repository import ApiMovieRepository

class MovieService:
    def __init__(self, movie_repository: ApiMovieRepository):
        self.movie_repository = movie_repository

    def get_popular_movies(self, page: int = 1) -> List[Movie]:
        return self.movie_repository.get_popular_movies(page=page)

    def search_movies(self, name_query: str = "", genre_query: str = "", date_query: str = "") -> List[Movie]:
        # Remove espaços em branco e converte para minúsculas as queries
        name_query = name_query.strip().lower()
        genre_query = genre_query.strip().lower()
        date_query = date_query.strip()

        # Se não houver nenhum filtro, retorna filmes populares
        if not name_query and not genre_query and not date_query:
            return self.get_popular_movies()

        # Obtém a lista base de filmes
        if name_query:
            # Se há busca por nome, usa a API de busca
            movies = self.movie_repository.search_movies_by_name(name_query)
        else:
            # Se não há busca por nome mas há outros filtros, usa filmes populares
            movies = self.get_popular_movies()

        # Filtra por gênero (client-side)
        if genre_query:
            movies = [
                movie for movie in movies
                if genre_query in movie.genre.lower()
            ]

        # Filtra por data de lançamento (client-side)
        if date_query:
            movies = [
                movie for movie in movies
                if date_query in movie.release_date
            ]

        return movies 