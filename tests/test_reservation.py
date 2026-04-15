import pytest
from src.classes.reservation import Reservation
from src.classes.adherent import Adherent
from src.classes.salle import Salle

@pytest.fixture
def setup_data():
    adherent = Adherent("Walid", 100, "ticket")
    salle = Salle("S1", "tennis", 10)
    return adherent, salle

def test_reservation_succes(setup_data):
    adherent, salle = setup_data
    reservation = Reservation(adherent, salle, "2026-04-18 20:30")
    reservation.confirmer()
    
    assert adherent.solde == 70
    assert salle.capacite == 9
    assert "Walid" in salle.inscrits

def test_reservation_solde_insuffisant(setup_data):
    adherent, salle = setup_data
    adherent.solde = 10
    reservation = Reservation(adherent, salle, "2026-04-18 20:30")
    
    with pytest.raises(ValueError, match="Solde insuffisant"):
        reservation.confirmer()

def test_mise_a_jour_registre_distant(setup_data, monkeypatch):
    """Utilise monkeypatch de pytest pour simuler l'appel réseau."""
    adherent, salle = setup_data

    # On crée une fonction factice qui simule requests.get(...).text
    class MockResponse:
        text = "Walid;2026-04-18 20:30\nOtmane;2026-04-18 21:30"

    def mock_get(*args, **kwargs):
        return MockResponse()

    # On remplace l'appel à requests.get par notre fonction mock_get
    import requests
    monkeypatch.setattr(requests, "get", mock_get)
    
    reservation = Reservation(adherent, salle, "2026-04-18 20:30")
    registre = reservation.recuperer_registre_distant("tennis")
    
    assert len(registre) == 2
    assert "Otmane;2026-04-18 21:30" in registre
