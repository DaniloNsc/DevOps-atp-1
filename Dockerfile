# syntax=docker/dockerfile:1

# ---- Estágio base ----
FROM python:3.12-slim AS base

# Evita geração de .pyc e força output sem buffer (bom para logs)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# ---- Estágio de dependências ----
FROM base AS deps

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Estágio final ----
FROM deps AS final

# Copia o código da aplicação
COPY main.py .

# Expõe a porta usada pelo Uvicorn
EXPOSE 8000

# Healthcheck para o container
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# Usuário não-root por segurança
RUN adduser --disabled-password --gecos "" appuser
USER appuser

# Comando de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
