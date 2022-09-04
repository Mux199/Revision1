import re

class Auto:
    def __init__(self, immat, modele, couleur, prix, marque="FakeBrand"):
        self.immat = immat
        assert re.match("^[A-Z]{1,2}-[0-9]{1,3}-[A-Z]{1,2} [0-9]{1,2}$", immat)
        self.marque = marque if marque != "FakeBrand" else "UNKNOWN"
        self.modele = modele
        self.couleur = couleur if couleur == "BLANCHE" or couleur == "NOIRE" or "GRISE" else "BLANCHE"
        self.prix = prix

    def __str__(self):
        return str(self.immat + " " + self.modele + " " + self.couleur + " " + str(self.prix) + " " + self.marque)

    def __eq__(self, other):
        return self.prix == other.prix and self.immat == other.immat and self.marque == other.marque and self.modele == other.modele and self.couleur == other.couleur

    def jsonize(self):
        return {
            "Immatriculation": self.immat,
            "Marque": self.marque,
            "Modele": self.modele,
            "Prix": self.prix,
            "Couleur": self.couleur
        }
