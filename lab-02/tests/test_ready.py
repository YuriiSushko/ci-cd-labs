def test_ready_with_file_storage(client):
    response = client.get("/ready")

    assert response.status_code == 200

    data = response.get_json()

    assert data["ready"] is True
    assert data["store"].startswith("file:")

def test_ready_returns_correct_file_path(client, tmp_path):
    response = client.get("/ready")

    assert response.status_code == 200

    data = response.get_json()
    expected_path = f"file:{tmp_path / 'visits.txt'}"

    assert data["store"] == expected_path