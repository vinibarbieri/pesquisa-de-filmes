import tkinter as tk
from app.repositories.file_movie_repository import FileMovieRepository
from app.services.auth_service import AuthenticationService
from app.services.movie_service import MovieService
from app.views.login_view import LoginView
from app.views.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.title("Sistema de Pesquisa de Filmes")
        self.geometry("750x550")

        # Configuração do grid da janela principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Instanciação dos serviços e repositório
        repo = FileMovieRepository("data/movies.json")
        self.auth_service = AuthenticationService()
        self.movie_service = MovieService(repo)

        # Inicialização da view atual
        self.current_view = None

        # Exibe a tela de login inicialmente
        self._show_login_view()

    def _show_login_view(self):
        # Remove a view atual se existir
        if self.current_view:
            self.current_view.destroy()

        # Cria e exibe a tela de login
        self.current_view = LoginView(
            parent=self,
            auth_service=self.auth_service,
            show_main_view_callback=self._show_main_view
        )

    def _show_main_view(self):
        # Remove a view atual se existir
        if self.current_view:
            self.current_view.destroy()

        # Cria e exibe a tela principal
        self.current_view = MainView(
            parent=self,
            movie_service=self.movie_service
        )

if __name__ == "__main__":
    app = App()
    app.mainloop() 