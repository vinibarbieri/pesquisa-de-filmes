import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
from app.services.auth_service import AuthenticationService

class LoginView(ttk.Frame):
    def __init__(self, parent, auth_service: AuthenticationService, show_main_view_callback: Callable):
        super().__init__(parent)
        self.auth_service = auth_service
        self.show_main_view_callback = show_main_view_callback

        # Configura o layout do frame
        self.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        # Cria os widgets
        self._create_widgets()

    def _create_widgets(self):
        # Label e Entry para usuário
        ttk.Label(self, text="Usuário:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Label e Entry para senha
        ttk.Label(self, text="Senha:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Botão de login
        login_button = ttk.Button(self, text="Login", command=self.handle_login)
        login_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Label para mensagens de status
        self.status_label = ttk.Label(self, text="")
        self.status_label.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Configura a coluna dos campos de entrada para expandir
        self.columnconfigure(1, weight=1)

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.auth_service.login(username, password):
            self.status_label.configure(text="Login bem-sucedido!", foreground="green")
            self.show_main_view_callback()
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha inválidos, ou falha na política de senha.")
            self.status_label.configure(text="Falha no login.", foreground="red") 