class Konto:
    def __init__(self, nr: str, betrag: int = 0): 
        self.nr = nr
        self.betrag = betrag
        self.administrator = None

    def set_administrator(self, admin):
        self.administrator = admin

    def einzahl(self, summe: int):
        if summe > 0:
            self.betrag += summe
            print(f"Konto {self.nr} + {summe} eingezahlt. Nueuer Kontostand: {self,betrag}")
        else:
            print("Der Einzahlungsbetrag muss grosser als 0 sein!")

    def auszahlen(self, summe: int):
        if summe <= 0:
            print("Der Auszahlungsbetrag muss grosser als 0 sein!")
        elif summe > self.betrag:
            print(f"Konto {self.nr} Auszahlung von {summe} nicht moglichl!")
        else:
            self.betrag -= summe
            print(f"Konto {self.nr} - {summe}")

    def __str__(self) -> str:
        return f"Konto(Nr = {self.nr}, Betrag = {self.betrag}, Admin = {self.administrator})" 

def main():
    konto1 = Konto("123")

    print(f"erzeught ohne Betrag: {konto1}")

    konto2 = Konto("345", 500)
    print(f"erzeught mit Betrag: {konto2}")

    konto1.set_administrator("Bob")
    konto2.set_administrator("Dob")

    konto1.einzahl(200)
    konto1.auszahlen(50)

    konto2.auszahlen(150)
    konto2.einzahl(600)

    print(konto1)
    print(konto2)

if __name__ == "__main__":
    main()

