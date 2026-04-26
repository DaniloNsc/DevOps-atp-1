from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# ─────────────────────────────────────────
# Testes do endpoint GET /
# ─────────────────────────────────────────

def test_root_status_code():
    """Verifica que o endpoint raiz retorna HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_root_status_field():
    """Verifica que o campo 'status' retorna 'ok'."""
    response = client.get("/")
    assert response.json()["status"] == "ok"


def test_root_message_field():
    """Verifica que o campo 'message' está presente e não é vazio."""
    response = client.get("/")
    data = response.json()
    assert "message" in data
    assert len(data["message"]) > 0


def test_root_timestamp_field():
    """Verifica que o campo 'timestamp' está presente na resposta."""
    response = client.get("/")
    data = response.json()
    assert "timestamp" in data


# ─────────────────────────────────────────
# Testes do endpoint GET /health
# ─────────────────────────────────────────

def test_health_status_code():
    """Verifica que o endpoint /health retorna HTTP 200."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_status_value():
    """Verifica que o campo 'status' retorna 'healthy'."""
    response = client.get("/health")
    assert response.json()["status"] == "healthy"


# ─────────────────────────────────────────
# Testes do endpoint GET /info
# ─────────────────────────────────────────

def test_info_status_code():
    """Verifica que o endpoint /info retorna HTTP 200."""
    response = client.get("/info")
    assert response.status_code == 200


def test_info_required_fields():
    """Verifica que todos os campos obrigatórios estão presentes em /info."""
    response = client.get("/info")
    data = response.json()
    assert "app" in data
    assert "tecnologia" in data
    assert "container" in data
    assert "ci_cd" in data


def test_info_docker_value():
    """Verifica que o campo 'container' menciona Docker."""
    response = client.get("/info")
    data = response.json()
    assert "Docker" in data["container"]


def test_info_github_actions_value():
    """Verifica que o campo 'ci_cd' menciona GitHub Actions."""
    response = client.get("/info")
    data = response.json()
    assert "GitHub Actions" in data["ci_cd"]


# ─────────────────────────────────────────
# Teste de rota inexistente
# ─────────────────────────────────────────

def test_not_found():
    """Verifica que rotas inexistentes retornam HTTP 404."""
    response = client.get("/rota-que-nao-existe")
    assert response.status_code == 404
