import json
from typing import List
from app.models.movie import Movie

class FileMovieRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_movies(self) -> List[Movie]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                movies_data = json.load(file)
                return [Movie(**movie_data) for movie_data in movies_data]
        except FileNotFoundError:
            print(f"Erro: Arquivo {self.file_path} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro: Falha ao decodificar JSON do arquivo {self.file_path}.")
            return [] 