import math

class Kreise:
    def __init__(self, x: float, y: float, radius: float): 
        if radius <= 0:
            raise ValueError("Der Radius muss positive sein!")
        self.x = x
        self.y = y
        self.radius = radius

    def verschieben(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def skalieren(self, faktor: float):
        if faktor > 0:
            self.radius *= faktor

    def umfang(self) -> float:
        return 2 * math.pi * self.radius

    def flaeche(self) -> float:
        return math.pi ** (self.radius ** 2)

    def __str__(self) -> str:
        return f"Kreis(Mittlepunkt = ({self.x}, {self.y}), Radius = {self.radius})" 

class Dreieck:
    def __init__(self, a: float, b: float, c: float): 
        self.nr = nr
        self.betrag = betrag
        self.administrator = None
    # ...

def main():
    circle = Kreise();

if __name__ == "__main__":
    main()
