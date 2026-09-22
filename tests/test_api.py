from fastapi.testclient import TestClient

from app.main import app



client = TestClient(app)

def test_health_check_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_analyze_returns_transparent_placeholder_response():
    response = client.post(
        "/api/v1/analyze",
        json={"text": "I feel overwhelmed today."},
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "analysis_status": "placeholder",
        "review_priority": "not_assessed",
        "received_text": "I feel overwhelmed today.",
        "message": "Analysis pipeline placeholder",
    }

def test_analyze_rejects_empty_text():
    response = client.post(
        "/api/v1/analyze",
        json={"text": ""},
    )

    assert response.status_code == 422

def test_analyze_rejects_whitespace_only_text():
    response = client.post(
        "/api/v1/analyze",
        json={"text": "   "},
    )

    assert response.status_code == 422