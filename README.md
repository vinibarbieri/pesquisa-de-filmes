# Sistema de Pesquisa de Filmes com TMDb API

Este é um aplicativo desktop desenvolvido em Python que permite pesquisar e filtrar filmes utilizando a API do The Movie Database (TMDb). O aplicativo oferece uma interface gráfica amigável para buscar filmes por nome, gênero e ano de lançamento.

## Funcionalidades

- **Busca por Nome**: Pesquisa filmes pelo título
- **Filtro por Gênero**: Filtra filmes por gênero (ex: Ação, Drama, Comédia)
- **Filtro por Ano**: Filtra filmes por ano de lançamento
- **Combinação de Filtros**: Permite combinar diferentes critérios de busca
- **Lista de Filmes Populares**: Exibe filmes populares quando nenhum filtro é aplicado
- **Interface Gráfica**: Interface amigável desenvolvida com Tkinter

## Requisitos

- Python 3.6 ou superior
- Conexão com a internet
- Chave de API do TMDb (v3)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/vinibarbieri/pesquisa-de-filmes.git
cd pesquisa-de-filmes
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com suas credenciais do TMDb:
```
TMDB_API_KEY=sua_chave_api_v3_aqui
TMDB_READ_ACCESS_TOKEN=seu_token_de_leitura_v4_aqui
```

## Como Obter as Credenciais do TMDb

1. Acesse [The Movie Database](https://www.themoviedb.org/)
2. Crie uma conta ou faça login
3. Acesse suas configurações de API
4. Solicite uma chave de API (v3)
5. Copie a chave e o token de acesso para o arquivo `.env`

## Estrutura do Projeto

```
.
├── app/
│   ├── models/
│   │   └── movie.py           # Modelo de dados para filmes
│   ├── repositories/
│   │   ├── api_movie_repository.py  # Integração com a API TMDb
│   │   └── user_repository.py       # Gerenciamento de usuários
│   ├── services/
│   │   ├── auth_service.py    # Serviço de autenticação
│   │   └── movie_service.py   # Lógica de negócio para filmes
│   └── views/
│       ├── login_view.py      # Interface de login
│       ├── main_view.py       # Interface principal
│       └── registration_view.py # Interface de registro
├── data/
│   └── users.json            # Armazenamento de usuários
├── .env                      # Credenciais da API
├── main.py                   # Ponto de entrada da aplicação
└── requirements.txt          # Dependências do projeto
```

## Como Usar

1. Execute o aplicativo:
```bash
python main.py
```

2. Faça login ou registre-se no sistema

3. Na tela principal, você pode:
   - Ver a lista de filmes populares
   - Pesquisar filmes por nome
   - Filtrar por gênero
   - Filtrar por ano de lançamento
   - Combinar diferentes filtros

## Funcionamento da Busca

O sistema utiliza diferentes estratégias de busca dependendo dos filtros aplicados:

1. **Busca por Nome**:
   - Utiliza o endpoint `/search/movie` da API TMDb
   - Filtros adicionais (gênero/ano) são aplicados localmente

2. **Busca por Gênero/Ano (sem nome)**:
   - Utiliza o endpoint `/discover/movie` da API TMDb
   - Aplica filtros diretamente na API para resultados mais precisos

3. **Sem Filtros**:
   - Exibe filmes populares usando o endpoint `/movie/popular`

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
