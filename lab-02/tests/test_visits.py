def test_visits_increments(client):
    first = client.get("/visits")
    second = client.get("/visits")

    assert first.status_code == 200
    assert second.status_code == 200

    assert first.get_json()["visits"] == 1
    assert second.get_json()["visits"] == 2


def test_visits_uses_file_storage(client):
    response = client.get("/visits")

    assert response.status_code == 200
    assert response.get_json()["store"] == "file"