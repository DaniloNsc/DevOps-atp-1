from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Atividade Formativa API", version="1.0.0")


@app.get("/")
def root():
    return {
        "message": "API funcionando com sucesso!",
        "timestamp": datetime.utcnow().isoformat(),
        "status": "ok"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/info")
def info():
    return {
        "app": "Atividade Formativa - Semanas 2, 3 e 4",
        "tecnologia": "Python + FastAPI",
        "container": "Docker",
        "ci_cd": "GitHub Actions"
    }
