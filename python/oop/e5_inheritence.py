import math

class Zaehler:
    def __init__(self): 
        self.stand = 0

    def weiterzaehlen(self):
        self.stand += 1

    def null_setzen(self):
        self.stand = 0

    def __str__(self) -> str:
        return f"Zaehlerstand: {self.stand}" 

class BegrenzterZaehler(Zaehler):
    def __init__(self, obergrenze: int): 
        super().__init__()
        self.obergrenze = obergrenze

    def weiterzaehlen(self):
        super().weiterzaehlen()
        if self.stand > self.obergrenze:
            super().null_setzen()

    def __str__(self) -> str:
        return f"Zaehler: {self.stand}" 

def main():
    verkehrs_zaehler = Zaehler()

    for _ in range(3):
        verkehrs_zaehler.weiterzaehlen()

    print(f"Nach 3 Autos: {verkehrs_zaehler}")

    verkehrs_zaehler.null_setzen()
    print(f"Nach Zurucksetzen: {verkehrs_zaehler}")

    sekunden = BegrenzterZaehler(59)
    sekunden.stand = 57
    verlauf_sek = []

    for _ in range(6):
        verlauf_sek.append(sekunden.stand)
        sekunden.weiterzaehlen()

    print(f"Sekundenzaehler {verlauf_sek}")

if __name__ == "__main__":
    main()
