from app.repositories.user_repository import UserRepository

class AuthenticationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def validate_password_policy(self, username: str, password: str) -> bool:
        # Verifica se a senha não está vazia
        if not password:
            return False

        # Verifica se a senha contém o nome de usuário (ignorando case)
        username_lower = username.lower()
        password_lower = password.lower()
        if username_lower in password_lower:
            return False

        return True

    def login(self, username: str, password: str) -> bool:
        # Primeiro, valida a política de senha
        if not self.validate_password_policy(username, password):
            print("Falha na política de senha.")
            return False

        # Verifica se o usuário existe e se a senha corresponde
        user = self.user_repository.find_user(username)
        if user and user["password"] == password:
            return True
        return False

    def register_user(self, username: str, password: str) -> bool:
        if not self.validate_password_policy(username, password):
            print("Falha na política de senha ao tentar registrar.")
            return False
        if self.user_repository.find_user(username):
            print("Nome de usuário já existe ao tentar registrar.")
            return False
        user_data = {"username": username, "password": password}
        return self.user_repository.add_user(user_data) 