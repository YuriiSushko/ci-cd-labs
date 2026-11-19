def test_health_returns_200(client):
    response = client.get("/health")

    assert response.status_code == 200


def test_health_returns_ok(client):
    response = client.get("/health")

    assert response.get_data(as_text=True) == "ok\n"