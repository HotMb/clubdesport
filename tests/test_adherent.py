import pytest
from src.classes.adherent import Adherent

@pytest.fixture
def adherent():
    return Adherent("Otmane", 100, "ticket")

def test_initialisation_adherent(adherent):
    """Vérifie qu'un adhérent est bien créé avec son nom, solde et abonnement."""
    assert adherent.nom == "Otmane"
    assert adherent.solde == 100
    assert adherent.type_abonnement == "ticket"

def test_calcul_prix_ticket(adherent):
    """Vérifie les tarifs pour un abonnement 'ticket'."""
    assert adherent.get_prix_seance("tennis") == 30
    assert adherent.get_prix_seance("badminton") == 20
    assert adherent.get_prix_seance("squash") == 15

def test_calcul_prix_forfait():
    """Vérifie les tarifs réduits pour un abonnement 'forfait'."""
    adherent = Adherent("Charlie", 100, "forfait")
    assert adherent.get_prix_seance("tennis") == 11
    assert adherent.get_prix_seance("badminton") == 10
    assert adherent.get_prix_seance("squash") == 9

def test_debit_solde_succes(adherent):
    """Vérifie que le solde diminue correctement après un paiement."""
    adherent.debit_solde(30)
    assert adherent.solde == 70

def test_debit_solde_insuffisant():
    """Vérifie qu'une erreur est levée si le solde est trop bas."""
    adherent = Adherent("Alice", 20, "ticket")
    with pytest.raises(ValueError, match="Solde insuffisant"):
        adherent.debit_solde(30)
