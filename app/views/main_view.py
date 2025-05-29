import tkinter as tk
from tkinter import ttk
from typing import List
from app.models.movie import Movie
from app.services.movie_service import MovieService

class MainView(ttk.Frame):
    def __init__(self, parent, movie_service: MovieService):
        super().__init__(parent)
        self.movie_service = movie_service

        # Configura o layout do frame
        self.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        # Cria os widgets
        self._create_widgets()

        # Carrega os filmes iniciais
        self.load_initial_movies()

    def _create_widgets(self):
        # Frame de Filtros
        filter_frame = ttk.LabelFrame(self, text="Filtros")
        filter_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Campos de filtro
        ttk.Label(filter_frame, text="Nome:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.name_entry = ttk.Entry(filter_frame)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

        ttk.Label(filter_frame, text="Gênero:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.genre_entry = ttk.Entry(filter_frame)
        self.genre_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

        ttk.Label(filter_frame, text="Data Lanç.:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.date_entry = ttk.Entry(filter_frame)
        self.date_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

        # Botão de pesquisa
        search_button = ttk.Button(filter_frame, text="Pesquisar", command=self.handle_search)
        search_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Configura a coluna dos campos de entrada para expandir
        filter_frame.columnconfigure(1, weight=1)

        # Frame de Resultados
        results_frame = ttk.LabelFrame(self, text="Resultados")
        results_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Listbox para resultados
        self.results_listbox = tk.Listbox(results_frame)
        self.results_listbox.pack(expand=True, fill="both", padx=5, pady=5)

        # Configura a linha do frame de resultados para expandir
        self.grid_rowconfigure(1, weight=1)

    def handle_search(self):
        name_query = self.name_entry.get()
        genre_query = self.genre_entry.get()
        date_query = self.date_entry.get()

        movies = self.movie_service.search_movies(name_query, genre_query, date_query)
        self._update_results_listbox(movies)

    def _update_results_listbox(self, movies: List[Movie]):
        self.results_listbox.delete(0, tk.END)
        for movie in movies:
            self.results_listbox.insert(tk.END, movie.title)

    def load_initial_movies(self):
        movies = self.movie_service.get_all_movies()
        self._update_results_listbox(movies) 