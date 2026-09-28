# FitManager — Desafio Django

Projeto desenvolvido para o desafio prático de Django da Aula 12.

## Tema
Gerenciador simples de treinos de academia.

## Funcionalidades
- Home
- Listagem de treinos
- Página de detalhes
- Cadastro de treino
- Edição de treino
- Exclusão com confirmação e POST
- Login/logout nativos do Django
- Proteção das ações de criar, editar e excluir com `@login_required`
- Botões de edição/exclusão ocultos para usuários não autenticados
- Herança de templates com `base.html`
- Bootstrap via CDN
- SQLite

## Como rodar

```bash
python -m venv venv
```

### Windows
```bash
venv\Scripts\activate
```

### Linux/macOS
```bash
source venv/bin/activate
```

Depois:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/treinos/
- http://127.0.0.1:8000/admin/
- http://127.0.0.1:8000/accounts/login/

## GitHub

```bash
git init
git add .
git commit -m "Projeto Django - Aula 12"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git
git push -u origin main
```
