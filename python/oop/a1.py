from random import randint

class Wuerfel:
    def __init__(self, augen, farbe): 
        self.augen = 1
        self.farbe = farbe
        self.augen = augen

    def werfen(self):
        self.augen = randint(1, 6)
        return self.augen


def main():
    wuerfel = Wuerfel(6, "Rot")
    versuche = 0

    while True:
        wuerfel.werfen()
        versuche += 1

        print(f"Wurf {versuche}: {wurfel.augen}")

        if wurfel.augen == 6:
            print(f"Geschafft! Nack {versuche} Wurfen wurde ein 6 gewurfelt")

if __name__ == "__main__":
    main()
