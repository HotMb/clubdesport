import pytest
from src.classes.salle import Salle

@pytest.fixture
def salle_tennis():
    """Crée une salle de tennis avec une capacité de 2 pour les tests."""
    return Salle("S1", "tennis", 2)

def test_initialisation_salle(salle_tennis):
    """Vérifie que la salle est bien initialisée."""
    assert salle_tennis.nom == "S1"
    assert salle_tennis.type_sport == "tennis"
    assert salle_tennis.capacite == 2
    assert len(salle_tennis.inscrits) == 0
    assert salle_tennis.est_disponible() is True

def test_ajouter_inscrit_succes(salle_tennis):
    """Vérifie qu'on peut ajouter un inscrit et que la capacité diminue."""
    salle_tennis.ajouter_inscrit("Walid")
    assert len(salle_tennis.inscrits) == 1
    assert "Walid" in salle_tennis.inscrits
    assert salle_tennis.capacite == 1
    assert salle_tennis.est_disponible() is True

def test_salle_devient_indisponible(salle_tennis):
    """Vérifie que la salle devient indisponible quand elle est pleine."""
    salle_tennis.ajouter_inscrit("Walid")
    salle_tennis.ajouter_inscrit("Otmane")
    assert salle_tennis.capacite == 0
    assert salle_tennis.est_disponible() is False

def test_ajouter_inscrit_erreur_salle_pleine(salle_tennis):
    """Vérifie qu'une erreur est levée si on ajoute quelqu'un dans une salle pleine."""
    salle_tennis.ajouter_inscrit("Walid")
    salle_tennis.ajouter_inscrit("Otmane")
    with pytest.raises(ValueError, match="Salle complète"):
        salle_tennis.ajouter_inscrit("Charlie")
