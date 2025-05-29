import json
import os
from typing import List, Dict, Optional

class UserRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file, indent=4, ensure_ascii=False)

    def _load_users(self) -> List[Dict[str, str]]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Erro: Arquivo {self.file_path} não encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Erro: Falha ao decodificar JSON do arquivo {self.file_path}.")
            return []

    def _save_users(self, users: List[Dict[str, str]]):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4, ensure_ascii=False)

    def find_user(self, username: str) -> Optional[Dict[str, str]]:
        users = self._load_users()
        username_lower = username.lower()
        
        for user in users:
            if user["username"].lower() == username_lower:
                return user
        
        return None

    def add_user(self, user_data: Dict[str, str]) -> bool:
        # Verifica se o usuário já existe
        if self.find_user(user_data["username"]):
            print("Erro: Nome de usuário já existe.")
            return False

        # Carrega a lista atual de usuários
        users = self._load_users()
        
        # Adiciona o novo usuário
        users.append(user_data)
        
        # Salva a lista atualizada
        self._save_users(users)
        
        return True 