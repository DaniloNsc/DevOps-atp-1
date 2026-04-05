# Atividade Formativa — Semanas 2, 3 e 4

API REST desenvolvida com **Python + FastAPI**, containerizada com **Docker** e com pipeline de **CI/CD via GitHub Actions**.

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python 3.12 |
| Framework | FastAPI |
| Servidor | Uvicorn |
| Container | Docker |
| CI/CD | GitHub Actions |

---

## 🚀 Rodando localmente (sem Docker)

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Acesse: http://localhost:8000/docs

---

## 🐳 Rodando com Docker

### Build da imagem
```bash
docker build -t atividade-formativa .
```

### Iniciar o container
```bash
docker run -d -p 8000:8000 --name minha-api atividade-formativa
```

### Verificar se está rodando
```bash
docker ps
```

### Acessar a API
- Raiz: http://localhost:8000/
- Health: http://localhost:8000/health
- Info: http://localhost:8000/info
- Documentação interativa: http://localhost:8000/docs

### Parar o container
```bash
docker stop minha-api
docker rm minha-api
```

---

## ✅ Testes

```bash
pip install pytest httpx
pytest test_main.py -v
```

---

## 🔄 CI/CD

O pipeline do GitHub Actions executa automaticamente a cada push ou PR para `main`:

1. **CI** — instala dependências e roda os testes com `pytest`
2. **CD** — faz o build da imagem Docker e valida a geração

> **Desafio opcional (DockerHub):** configure os secrets `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN` no repositório e descomente o job `docker-publish` no workflow.

---

## 📁 Estrutura do projeto

```
.
├── main.py                        # Aplicação FastAPI
├── test_main.py                   # Testes automatizados
├── requirements.txt               # Dependências Python
├── Dockerfile                     # Configuração do container
├── .dockerignore                  # Arquivos ignorados pelo Docker
└── .github/
    └── workflows/
        └── ci-cd.yml              # Pipeline CI/CD
```
## 👨‍💻 Autor: Danilo Gabriel do Nascimento!

<div align="center">

Feito **Atividade Somativa 1**

[![GitHub](https://img.shields.io/badge/GitHub-SEU_USUARIO-181717?style=for-the-badge&logo=github)](https://github.com/SEU_USUARIO)

</div>

