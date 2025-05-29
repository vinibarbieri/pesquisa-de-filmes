import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
from app.services.auth_service import AuthenticationService

class RegistrationView(ttk.Frame):
    def __init__(self, parent, auth_service: AuthenticationService, show_login_view_callback: Callable):
        super().__init__(parent)
        self.auth_service = auth_service
        self.show_login_view_callback = show_login_view_callback

        self.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="Usuário:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(self, text="Senha:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(self, text="Confirmar Senha:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.confirm_password_entry = ttk.Entry(self, show="*")
        self.confirm_password_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        register_button = ttk.Button(self, text="Registrar", command=self.handle_register)
        register_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        back_button = ttk.Button(self, text="Voltar para Login", command=self.show_login_view_callback)
        back_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.status_label = ttk.Label(self, text="")
        self.status_label.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.columnconfigure(1, weight=1)

    def handle_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not password or not confirm_password:
            messagebox.showwarning("Campos Vazios", "Todos os campos são obrigatórios.")
            return
        if password != confirm_password:
            messagebox.showwarning("Senhas Divergentes", "As senhas não coincidem.")
            return
        if self.auth_service.register_user(username, password):
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso! Faça o login.")
            self.status_label.configure(text="Usuário registrado com sucesso!", foreground="green")
            self.show_login_view_callback()
        else:
            messagebox.showerror("Falha no Registro", "Não foi possível registrar o usuário. Verifique os dados ou o console para mais detalhes.")
            self.status_label.configure(text="Falha no registro.", foreground="red") 