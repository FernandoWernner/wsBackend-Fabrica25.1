# Rick And Morty API - Django

### Caso preferir fiz uma breve documentação no Notion: https://rhetorical-quail-2ca.notion.site/Fabrica-25-1-1a90e012d08e8082b0bbf9f68a9e1e9c?pvs=73

Este é um projeto Django que consome a API do Rick & Morty e permite visualizar e adicionar personagens.

## Instalação

1. Clone este repositório:

git clone https://github.com/FernandoWernner/wsBackend-Fabrica25.1.git

2. Entre na pasta do projeto:

cd rickmortyapi

3. Crie e ative um ambiente virtual:

python -m venv venv

4. Instale as dependências:

pip install -r requirements.txt

5. Rode as migrações do banco de dados:

python .\manage.py migrate

6. Execute o servidor:

python .\manage.py runserver

### Caso execute usando o django-admin não vai funcionar

7. Acesse a API em:

http://127.0.0.1:8000/api/

http://127.0.0.1:8000/api/api/Personagens/

http://127.0.0.1:8000/api/api/Episódios/

