# TODO - Redirecionar /admin/login/ para tela customizada + listagens

## Objetivo
Redirecionar `/admin/login/` para a tela de login customizada `/admin-login/` e exibir nela as listagens de registro/informações da associação.

## Passos
- [x] 1. Analisar arquivos relevantes (views.py, urls.py, admin_login.html, admin.py, models.py)
- [x] 2. Adicionar view `redirect_admin_login` em `associacao/views.py`
- [x] 3. Adicionar contexto de listagens/contagens à view `admin_login`
- [x] 4. Adicionar rota `admin/login/` em `core/urls.py`
- [x] 5. Adicionar campo oculto `next` + seção de listagens no `admin_login.html`
- [x] 6. Verificar com `python manage.py check`
