import math

class Auto:
    def __init__(self, marke: str, modell: str, baujaher: int, farbe: str): 
        self.marke = marke
        self.modell = modell
        self.baujaher = baujaher
        self.farbe = farbe

    def __str__(self) -> str:
        return f"{self.marke} {self.modell}, ({self.baujaher}, {self.farbe})" 

class Statistics:

    def __init__(self, autos: list):
        self.autos = autos

    def anzahl_nach_farbe(self, gesuchte_farbe: str) -> int:
        anzahl = 0
        for auto in self.autos:
            if auto.farbe.lower() == gesuchte_farbe.lower():
                anzahl += 1

        return anzahl

    def durchschnittliche_baujahr(self, gescuhte_marke: str) -> float:
        summe_baujahr = 0
        anzahl = 0

        for auto in self.autos:
            if auto.marke.lower() == gescuhte_marke.lower():
                summe_baujahr += auto.baujaher
                anzahl += 1

        if anzahl == 0.0:
            return 0.0

        return summe_baujahr / anzahl


def main():
    autoliste = [
        Auto("Dacia", "Logan", 2018, "Rot"),
        Auto("Dacia", "Papuc", 2005, "Gelb"),
        Auto("Dacia", "Sandero", 2022, "Schwarz"),
        Auto("Audi", "A6", 2016, "Weis"),
        Auto("BMW", "e60", 2005, "rot"),
    ]

    stats = Statistics(autoliste)

    farbe = "Rot"

    anzahl_rot = stats.anzahl_nach_farbe(farbe)
    print(f"Anzahl der Autos mit der Farbe '{farbe}': {anzahl_rot}")

    marke = "Dacia"
    schniit_baujahr = stats.durchschnittliche_baujahr(marke)
    print(f"Durchschnittliche_baujahr Baujahr der Marke {marke}: {schniit_baujahr}")

if __name__ == "__main__":
    main()
