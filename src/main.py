from src.classes.adherent import Adherent
from src.classes.salle import Salle
from src.classes.reservation import Reservation

def demo():
    print("=== DÉMONSTRATION DU CLUB DE SPORT ===")
    
    # 1. Création d'une salle de Tennis (2 places)
    salle_tennis = Salle("Court Central", "tennis", 2)
    print(f"Nouvelle salle : {salle_tennis.nom} ({salle_tennis.type_sport})")
    
    # 2. Création d'un adhérent avec 300€
    walid = Adherent("Walid", 300)
    print(f"Nouvel adhérent : {walid.nom} (Solde: {walid.solde}€, Type: {walid.abonnement.type_abo})")
    
    # 3. Passage au forfait (Coût: 200€)
    print("\n--- Souscription au forfait ---")
    walid.souscrire_forfait()
    print(f"Solde après forfait : {walid.solde}€ (Type: {walid.abonnement.type_abo})")
    
    # 4. Réservation d'une séance (Coût: 11€ pour le tennis au forfait)
    print("\n--- Réservation d'une séance de Tennis ---")
    res = Reservation(walid, salle_tennis, "2026-04-15 15:30")
    res.confirmer()
    
    # 5. État final
    print(f"Réservation confirmée pour {walid.nom} !")
    print(f"Solde final de Walid : {walid.solde}€")
    print(f"État de la salle : {len(salle_tennis.inscrits)} inscrit(s), places restantes : {salle_tennis.capacite}")

if __name__ == "__main__":
    demo()