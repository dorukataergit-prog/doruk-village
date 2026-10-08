from backend.app import app


def test_app_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "ok"
