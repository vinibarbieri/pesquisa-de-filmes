import tkinter as tk
import os
from dotenv import load_dotenv
from app.repositories.api_movie_repository import ApiMovieRepository
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthenticationService
from app.services.movie_service import MovieService
from app.views.login_view import LoginView
from app.views.main_view import MainView
from app.views.registration_view import RegistrationView

# Load environment variables
load_dotenv()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Load TMDb API key
        self.tmdb_api_key = os.getenv("TMDB_API_KEY")
        if not self.tmdb_api_key:
            print("ERRO: Chave de API TMDB_API_KEY não encontrada no arquivo .env!")
            self.destroy()
            return

        # Configuração da janela principal
        self.title("Sistema de Pesquisa de Filmes")
        self.geometry("750x550")

        # Configuração do grid da janela principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Instanciação dos serviços e repositório
        self.user_repo = UserRepository("data/users.json")
        api_repo = ApiMovieRepository(api_key=self.tmdb_api_key)
        self.auth_service = AuthenticationService(self.user_repo)
        self.movie_service = MovieService(api_repo)

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
            show_main_view_callback=self._show_main_view,
            show_registration_view_callback=self._show_registration_view
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

    def _show_registration_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = RegistrationView(
            parent=self,
            auth_service=self.auth_service,
            show_login_view_callback=self._show_login_view
        )

if __name__ == "__main__":
    app = App()
    app.mainloop() 