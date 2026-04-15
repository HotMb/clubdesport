import pytest
from src.classes.abonnement import Abonnement

def test_abonnement_ticket():
    """Vérifie qu'un abonnement au ticket ne coûte rien au début."""
    abo = Abonnement("ticket")
    assert abo.type_abo == "ticket"
    assert abo.get_cout_initial() == 0
    assert abo.get_prix_sport("tennis") == 30

def test_abonnement_forfait():
    """Vérifie qu'un abonnement au forfait coûte 200€ initialement."""
    abo = Abonnement("forfait")
    assert abo.type_abo == "forfait"
    assert abo.get_cout_initial() == 200
    assert abo.get_prix_sport("tennis") == 11

def test_prix_sport_inconnu():
    """Vérifie qu'un sport inconnu retourne un prix de 0."""
    abo = Abonnement("ticket")
    assert abo.get_prix_sport("otmane") == 0
