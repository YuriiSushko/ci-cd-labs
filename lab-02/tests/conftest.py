import pytest
import app as shop


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(shop, "DATABASE_URL", None)
    monkeypatch.setattr(shop, "COUNTER_FILE", tmp_path / "visits.txt")

    shop.app.config.update(TESTING=True)

    with shop.app.test_client() as client:
        yield client