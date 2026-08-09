# TODO - Configuração de Deploy (Vercel)

## Objetivo
Corrigir e otimizar a configuração de deploy do site Django ASSGA para a Vercel.

## Passos

- [x] 1. Corrigir `vercel.json` (entrada WSGI `core/wsgi.py`, rotas static/media, env vars `DEBUG`)
- [x] 2. Melhorar `build.sh` (migrations, superuser opcional, collectstatic, criar `public/`)
- [x] 3. Preencher/corrigir `build_files.sh`
- [x] 4. Revisar `core/wsgi.py` (manter como entrada Vercel)
- [x] 5. Revisar `wsgi_config.py` (evitar conflito)
- [x] 6. Atualizar `.gitignore` (adicionar `public/`, `media/`, etc)
- [ ] 7. Testar localmente (migrate + collectstatic + runserver)
- [ ] 8. Documentar instruções de deploy (README)

## Observações
- `requirements.txt` tem `Django==6.0.5` (válido, existe no pip)
- SQLite NÃO persiste na Vercel — para dados permanentes usar PostgreSQL (`DATABASE_URL`)
