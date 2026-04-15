import pytest
import requests

@pytest.fixture(autouse=True)
def mock_remote_registry(monkeypatch):
    """
    Cette fixture s'exécute AUTOMATIQUEMENT avant chaque test.
    Elle simule la réponse du site web pour tous les tests du projet.
    """
    class MockResponse:
        text = "Walid;2026-04-18 20:30\nOtmane;2026-04-18 21:30"

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)