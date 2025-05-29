class AuthenticationService:
    def __init__(self):
        self.users = {
            "admin": "AbcAdmin123",
            "usuario": "SenhaComUser",
            "teste": "Teste123!"
        }

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
        stored_password = self.users.get(username)
        if stored_password is None or stored_password != password:
            return False

        return True 