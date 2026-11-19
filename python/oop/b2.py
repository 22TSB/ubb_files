import math

class Bruch:
    def __init__(self, z: int, n: int): 
        if n == 0:
            raise ValueError("Der Nenner darf nicht 0 sein!")
        self.zaehler = z
        self.nenner = n

    def erweitern(self, k: int):
        if k == 0:
            raise ValueError("Mit 0 darf nicht erweitert weden!")

        self.zaehler *= k
        self.nenner *= k

    def kuerzen(self, k: int):
        if k == 0:
            raise ValueError("Durch 0 darf nicht gekurzt weden!")

        self.zaehler //= k
        self.nenner //= k

    def vollstaendingKurzen(self):
        ggt = math.gcd(self.zaehler, self.nenner)
        self.kuerzen(ggt)

    def __str__(self) -> str:
        return f"{self.zaehler}/{self.nenner}" 


def main():
    b = Bruch(4, 6)
    print(f"Startbruch: {b}")
    b.erweitern(3)
    print(f"Nach b.erweitern(): {b}")
    b.kuerzen(2)
    print(f"Nach b.kurzen(): {b}")
    print(f"b.zaehler(): {b.zaehler}")
    print(f"b.nenner(): {b.nenner}")
    b.vollstaendingKurzen()
    print(f"Nach vollstanding(): (Zahler: {b.zaehler}, Nenner: {b.nenner})")

if __name__ == "__main__":
    main()

