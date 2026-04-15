import pytest
from src.classes.adherent import Adherent

@pytest.fixture
def adherent_ticket():
    return Adherent("Walid", 100, "ticket")

def test_initialisation_ticket(adherent_ticket):
    """Le solde ne bouge pas pour un ticket (coût 0€)."""
    assert adherent_ticket.solde == 100
    assert adherent_ticket.nom == "Walid"

def test_passage_au_forfait():
    """Vérifie que le passage au forfait déduit bien 200€."""
    adherent = Adherent("Otmane", 500, "ticket")
    
    adherent.souscrire_forfait()
    
    assert adherent.abonnement.type_abo == "forfait"
    assert adherent.solde == 300 # 500€ - 200€
    assert adherent.get_prix_seance("tennis") == 11

def test_prix_seance_via_abonnement(adherent_ticket):
    """Vérifie que l'adhérent récupère les prix depuis son objet abonnement."""
    assert adherent_ticket.get_prix_seance("tennis") == 30

def test_debit_solde_succes(adherent_ticket):
    adherent_ticket.debit_solde(30)
    assert adherent_ticket.solde == 70

def test_debit_solde_insuffisant():
    adherent = Adherent("Alice", 10, "ticket")
    with pytest.raises(ValueError, match="Solde insuffisant"):
        adherent.debit_solde(30)

def test_passage_au_forfait_solde_insuffisant():
    """Vérifie qu'on ne peut pas passer au forfait si on n'a pas les 200€."""
    adherent = Adherent("Walid", 50, "ticket")
    with pytest.raises(ValueError, match="Solde insuffisant"):
        adherent.souscrire_forfait()
